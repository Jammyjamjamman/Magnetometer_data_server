#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:06:40 2018

@author: james
"""
from pymongo import MongoClient


def write_mag_dat(mag_dat,
                  sensor_id="HAD",
                  db_host="localhost",
                  magw_usr="Magnetwriter",
                  magw_pass="magpassword"):
    """Write raw sensor readings, as a list of dictionaries, to the database."""
    
    def get_mag_writer(db_host, magw_usr, magw_pass):
        """Returns the cursor for inserting into 
        the magnetic data region of the mongo database."""
        return MongoClient(db_host,
                           username=magw_usr,
                           password=magw_pass,
                           authSource="mag_db")["mag_db"]["magnetDat"]
    
    # Get the magnetic data write cursor.
    sen_writer = get_mag_writer(db_host, magw_usr, magw_pass)
    # Include the sensor_id for the inserts.
    for dat in mag_dat:
        dat["observatories_id"] = sensor_id
    # Insert data into the database.
    sen_writer.insert_many(mag_dat)


def write_raw_dat(raw_dat,
                  sensor_id="HAD",
                  db_host="localhost",
                  senw_usr="Sensorwriter",
                  senw_pass="senpassword"):
    """Write raw sensor readings, as a list of dictionaries, to the database."""
        
    def get_sen_writer(db_host, senw_usr, senw_pass):
        """Returns the cursor for inserting into 
        the raw data region of the mongo database."""
        return MongoClient(db_host,
                           username=senw_usr,
                           password=senw_pass,
                           authSource="mag_db")["mag_db"]["sensorDat"]    
    # Get the raw data write cursor.
    sen_writer = get_sen_writer(db_host, senw_usr, senw_pass)
    # Include the sensor_id for identifying the inserts.
    for dat in raw_dat:
        dat["observatories_id"] = sensor_id
    # Insert data into the database.
    sen_writer.insert_many(raw_dat)
