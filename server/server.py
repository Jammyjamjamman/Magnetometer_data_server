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
cors = CORS(app, resources="/available_sensors")

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
    """Loads the homepage for a new client connection.
    
    Returns:
        str: The homepage.
    """
    with open("index.html", 'r') as homepage:
        return homepage.read()


@app.route("/available_sensors")
def available_sensors():
    """Gets the sensors available in the database.
    Returns:
        str: the list of sensors available as a json string.
    """
    return jsonify(list(mongo_queries.get_available_sensors()))


def listdict_csv_iter(dict_list):
    """Convert a list of dicts to a csv, as an iterator.
    
    Args:
        dict_list (Iter(dict)): An iterable which yields a dictionaries, all
        with the same keys.
    
    Yields:
        str: A string which represents a line of a csv file.
    """
    # Iterate through the list of dictionaries
    for dat in dict_list:
        try:
            # Generate the next line of the csv
            yield csv_row_fmt.format(**dat)
        except NameError:
            # Generate the Header and the first line of the csv, if this
            # does not exist yet.
            yield ",".join(dat.keys()) + '\n'
            csv_row_fmt = "{" + "},{".join(dat.keys()) + "}\n"
            yield csv_row_fmt.format(**dat)


@app.route("/mag_dat")
def download_mag_dat():
    """
    Download magnetometer data.
    
    Returns:
        Response: A csv containing magnetometer data.
    """
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
    return Response(listdict_csv_iter(dat), mimetype='text/csv')


@app.route("/raw_dat")
def download_raw_dat():
    """
    Download raw data.
    
    Returns:
        Response: A csv containing raw data.
    """
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
        
    dat = mongo_queries.get_raw_dat(sensor_id, starttime, endtime)
    return Response(listdict_csv_iter(dat), mimetype='text/csv')


if __name__ == "__main__":
    app.run(debug=True)
