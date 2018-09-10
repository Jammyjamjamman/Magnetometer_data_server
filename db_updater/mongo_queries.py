#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 12:50:55 2018

@author: james
"""
import mongo_cursors


def get_conditions(sensor_id, starttime, endtime):  
    conditions = {"$and": [{"sensor_id": sensor_id}]}
    if starttime is not None:
        conditions["$and"].append({"time": {"$gte": starttime}})
    if endtime is not None:
        conditions["$and"].append({"time": {"$lte": endtime}})
    
    return conditions


def get_available_sensors():
    read_cursor = mongo_cursors.get_read_cursor()
    return read_cursor.observatories.find()


def get_raw_dat(sensor_id, starttime=None, endtime=None):
    read_cursor = mongo_cursors.get_read_cursor()
    conditions = get_conditions(sensor_id, starttime, endtime)
    return read_cursor.sensorDat.find(conditions, {"_id": 0}).sort([("time", 1)])
 
    
def get_mag_dat(sensor_id, starttime=None, endtime=None):
    read_cursor = mongo_cursors.get_read_cursor()
    conditions = get_conditions(sensor_id, starttime, endtime)
    return read_cursor.magnetDat.find(conditions, {"_id": 0}).sort([("time", 1)])


def insert_sensor(sensor_dat_dict):
    obs_writer = mongo_cursors.get_obs_writer()
    obs_writer.insert_one(sensor_dat_dict)
