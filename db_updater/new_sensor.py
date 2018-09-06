#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 10:28:37 2018

@author: james
"""
import mongo_queries
from mongo_cursors import get_passwords, DB_HOST, SENW_USR, MAGW_USR


def add_sensor(sensor_id, latitude, longitude, elevation, coord_sys, insert_params, **kwargs):
    """
    Add a sensor and its details to the mongo database. A script is also
    generated, which contains functions for inserting sensor readings into the
    database.
    """
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
    
    passwords = get_passwords()
    
    # Set the database location, usernames and passwords in the sensor script.
    template_script = template_script.replace('sensor_id=""', 'sensor_id="'+sensor_id+'"')
    template_script = template_script.replace('db_host=""', 'db_host="'+DB_HOST+'"')
    template_script = template_script.replace('magw_usr=""', 'magw_usr="'+MAGW_USR+'"')
    template_script = template_script.replace('magw_pass=""', 'magw_pass="'+passwords[MAGW_USR]+'"')
    template_script = template_script.replace('senw_usr=""', 'senw_usr="'+SENW_USR+'"')
    template_script = template_script.replace('senw_pass=""', 'senw_pass="'+passwords[SENW_USR]+'"')


    script_name = sensor_id+"_dat_insert.py"
    
    with open(script_name, 'w') as insert_script:
        insert_script.write(template_script)
        
    print("New sensor script generated. The script can be used to insert raw"
          " sensor data to the database using write_raw_dat(). write_mag_dat()"
          " can be used to write processed magnetometer data to the database."
          " The script can be found in this directory with the filename:", script_name)