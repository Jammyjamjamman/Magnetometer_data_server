#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 12:22:21 2018

@author: james
"""

from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import mongo_queries
from datetime import datetime

app = Flask(__name__)
cors = CORS(app, resources="/available-sensors")

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/')
def root():
    with open("index.html", 'r') as homepage:
        return homepage


@app.route("/available-sensors")
def available_sensors():
    return jsonify(list(mongo_queries.get_available_sensors()))


def listdict_csv_iter(dict_list):
    """Convert a list of dicts to a csv, as an iterator."""
    for dat in dict_list:
        try:
            yield csv_row_fmt.format(**dat)
        except NameError:
            yield ",".join(dat.keys()) + '\n'
            csv_row_fmt = "{" + "},{".join(dat.keys()) + "}\n"
            yield csv_row_fmt.format(**dat)


@app.route("/mag-dat")
def download_mag_dat():
    # The request is invalid if a user does not provide a sensor ID.
    sensor_id = request.args.get("sensor_id")
    if sensor_id is None:
        raise InvalidUsage("Sensor ID not provided!", status_code=400)
    try:
        starttime = datetime.fromtimestamp(int(request.args.get("starttime")))
    except TypeError:
        starttime = None
    try:
        endtime = datetime.fromtimestamp(int(request.args.get("endtime")))
    except TypeError:
        endtime = None
        
    dat = mongo_queries.get_mag_dat(sensor_id, starttime, endtime)
    return Response(dat, mimetype='text/csv')
#    
#    with open("download_test.zip", "rb") as dl_file:
#        return send_file(io.BytesIO(dl_file.read()), mimetype="application/zip")

@app.route("/raw-dat")
def download_raw_dat():
    # The request is invalid if a user does not provide a sensor ID.
    sensor_id = request.args.get("sensor_id")
    if sensor_id is None:
        raise InvalidUsage("Sensor ID not provided!", status_code=400)
    starttime = request.args.get("starttime")
    endtime = request.args.get("endtime")
    return (str(sensor_id) + starttime + str(endtime))

if __name__ == "__main__":
    app.run(debug=True)
