#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:06:40 2018

@author: james
"""
from pymongo import MongoClient


def get_sen_writer(db_host="localhost"):
    """Returns the cursor for inserting into 
    the raw sensor region of the mongo database."""
    return MongoClient(db_host,
                       username="Magnetwriter",
                       password="magpassword",
                       authSource="mag_db")["mag_db"]["magnetDat"]


def write_mag_dat(mag_dat, sensor_id="frg_single_fgm3"):
    """Write a list of dictionaries representing magnetometer readings to the database."""
    # Get the write cursor.
    sen_writer = get_sen_writer()
    # Include the sensor_id for the inserts.
    for dat in mag_dat:
        dat["observatories_id"] = sensor_id
    # Insert data into the database.
    sen_writer.insert_many(mag_dat)
    

def write_raw_dat(raw_dat, sensor_id="frg_single_fgm3"):
    """Write a list of dictionaries representing sensor readings to the database."""
    
    # Get the write cursor.
    sen_writer = get_sen_writer()
    # Include the sensor_id for identifying the inserts.
    for dat in raw_dat:
        dat["observatories_id"] = sensor_id
    # Insert data into the database.
    sen_writer.insert_many(raw_dat)
        
