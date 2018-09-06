#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 10:28:37 2018

@author: james
"""
import mongo_queries
from mongo_cursors import get_passwords


def add_sensor(sensor_id, latitude, longitude, elevation, coord_sys, insert_params, **kwargs):
    """Add a sensor to the mongo database."""
    sensor_info = {}
    sensor_info["_id"] = sensor_id
    sensor_info["latitude"] = latitude
    sensor_info["longitude"] = longitude
    sensor_info["elevation"] = elevation
    sensor_info["coord_sys"] = coord_sys
    sensor_info = {**sensor_info, **kwargs}
    mongo_queries.insert_sensor(sensor_info)
    generate_mongoconn_script(sensor_info["_id"])


def generate_mongoconn_script(sensor_id):
    template_script = ""
    with open("insert_sendat_template.py", 'r') as template_file:
        template_script = template_file.read()
    
    template_script = template_script.replace('sensor_id=""', 'sensor_id="'+sensor_id+'"')
    script_name = sensor_id+"_dat_insert.py"
    
    with open(script_name, 'w') as insert_script:
        insert_script.write(template_script)
        
    print("New sensor script generated. It can be found in this directory with"
          " the filename:", script_name)