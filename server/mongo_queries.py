#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 12:50:55 2018

@author: james
"""
import mongo_cursors


def get_conditions(sensor_id, starttime, endtime):
    """
    Helper function to reformat the sensor conditions as a python dictionary,
    for querying the mongo database.
    """
    conditions = {"$and": [{"observatories_id": sensor_id}]}
    if starttime is not None:
        conditions["$and"].append({"time": {"$gte": starttime}})
    if endtime is not None:
        conditions["$and"].append({"time": {"$lte": endtime}})
    
    return conditions


def get_available_sensors():
    """
    Gets the sensors present in the database, as a list of dictionaries.
    Returns:
        List(dict): A list of dictionaries, where each dictionary contains
        information about a sensor
    """
    read_cursor = mongo_cursors.get_read_cursor()
    return read_cursor.observatories.find()


def get_raw_dat(sensor_id, starttime=None, endtime=None):
    """
    Gets raw magnetometer data from the magnetometer database. The data
    is sorted in ascending time.
    
    Args:
        sensor_id (str): The observatory ID of the sensor.
        starttime (datetime): The lower time bound to get data within.
        endtime (datetime): The upper time bound to get data within.
        
    Returns:
        pymongo.mongoClient cursor: A mongodb cursor, which returns
        dictionaries in the form {"time": datetime(), ...}
    """
    read_cursor = mongo_cursors.get_read_cursor()
    conditions = get_conditions(sensor_id, starttime, endtime)
    # Do not include the id of each row element or the observatory id of the 
    # data, as these are not useful.
    return read_cursor.sensorDat.find(conditions, {"_id": 0, "observatories_id": 0}).sort([("time", 1)])
 
    
def get_mag_dat(sensor_id, starttime=None, endtime=None):
    """
    Gets magnetometer data from the magnetometer database. The data is sorted
    in ascending time.
    
    Args:
        sensor_id (str): The observatory ID of the sensor.
        starttime (datetime): The lower time bound to get data within.
        endtime (datetime): The upper time bound to get data within.
        
    Returns:
        pymongo.mongoClient cursor: A mongodb cursor, which returns
        dictionaries in the form {"time": datetime(), ...}
    """
    read_cursor = mongo_cursors.get_read_cursor()
    conditions = get_conditions(sensor_id, starttime, endtime)
    print(conditions)
    # Do not include the id of each row element or the observatory id of the 
    # data, as these are not useful.
    return read_cursor.magnetDat.find(conditions, {"_id": 0, "observatories_id": 0}).sort([("time", 1)])