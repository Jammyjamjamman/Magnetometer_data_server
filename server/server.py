#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 12:22:21 2018

@author: james
"""

from flask import Flask, Response, send_file, request, jsonify
from flask_cors import CORS
import mongo_queries

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
def download_button():
    download_html = """<!DOCTYPE html>
                        <html>
                        <body>
                        
                        <p>Click on the w3schools logo to download the image:<p>
                        
                        <a href="/download_test" download>Download now!</a>
                        
                        <p><b>Note:</b> The download attribute is not supported in Edge version 12, IE, Safari 10 (and earlier), or Opera version 12 (and earlier).</p>
                        
                        </body>
                        </html>"""
    return download_html


@app.route("/available-sensors")
def available_sensors():
    return jsonify(list(mongo_queries.get_available_sensors()))


@app.route("/download-test")
def download_stream():
    sensor_id = request.args.get("sensor_id")
    if sensor_id is None:
        raise InvalidUsage("Sensor ID not provided!", status_code=400)
    starttime = request.args.get("starttime")
    endtime = request.args.get("endtime")
    return (str(sensor_id) + starttime + str(endtime))
#    def return_csv():
#        fieldnames = ["time", "reading", "temperature"]
#        yield ",".join(fieldnames) + '\n'
#        
#        for dat in query_mag.get_all_frg_dat():
#            yield "{time},{reading},{temperature}\n".format(**dat)
#    
#    with open("download_test.zip", "rb") as dl_file:
#        return send_file(io.BytesIO(dl_file.read()), mimetype="application/zip")


if __name__ == "__main__":
    app.run(debug="True")