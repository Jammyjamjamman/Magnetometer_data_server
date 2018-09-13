#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:06:40 2018

@author: james
"""
from pymongo import MongoClient


def write_mag_dat(mag_dat,
                  sensor_id="",
                  db_host="",
                  magw_usr="",
                  magw_pass=""):
    """
    Write magnetometer readings, as a list of dictionaries, to the database.
    
    Args:
        mag_dat (List(dict)): The magnetometer readings. Each
        dictionary in the list is expected to have at least a datetime with 
        the key "time" and a magnetometer reading value.
        sensor_id (str): The id of the sensor inserting data.
        db_host (str): The database url.
        magw_usr (str): the username for writing to the magnetDat collections.
        magw_pass (str): the password for writing to the magnetDat collections.
    """
    
    def get_mag_writer(db_host, magw_usr, magw_pass):
        """
        Returns the cursor for inserting into the magnetic data region of
        the mongo database.
        
        Args:
            db_host (str): The database url.
            magw_usr (str): the username for writing to the sensor area of the
            database.
            magw_pass (str): the password for writing to the sensor area of the
            database.
        """
        return MongoClient(db_host,
                           username=magw_usr,
                           password=magw_pass,
                           authSource="mag_db")["mag_db"]["magnetDat"]
    
    # Get the magnetic data write cursor.
    mag_writer = get_mag_writer(db_host, magw_usr, magw_pass)
    # Include the sensor_id for the inserts.
    for dat in mag_dat:
        dat["observatories_id"] = sensor_id
    # Insert data into the database.
    mag_writer.insert_many(mag_dat)


def write_raw_dat(raw_dat,
                  sensor_id="",
                  db_host="",
                  senw_usr="",
                  senw_pass=""):
    """
    Write raw sensor readings, as a list of dictionaries, to the database.
    
    Args:
        raw_dat (List(dict)): The raw sensor readings. Each dictionary in the
        list is expected to have at least a datetime with the key "time" and a
        sensor reading value.
        sensor_id (str): The id of the sensor inserting data.
        db_host (str): The database url.
        magw_usr (str): the username for writing to the sensor area of the
        database.
        magw_pass (str): the password for writing to the sensor area of the
        database.
    """
        
    def get_sen_writer(db_host, senw_usr, senw_pass):
        """
        Returns the cursor for inserting into the raw data region of
        the mongo database.
        
        Args:
            db_host (str): The database url.
            magw_usr (str): the username for writing to the sensorDat collections.
            magw_pass (str): the password for writing to the SensorDat collections.
            database.
        """
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
