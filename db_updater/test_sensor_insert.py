#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 22:53:22 2018

@author: james
"""
DB_LOC = "localhost"

from pymongo import MongoClient


def get_rw_cursor(usr, password, db_host):
    return MongoClient(db_host,
                       username=usr,
                       password=password,
                       authSource="mag_db")["mag_db"]


def check_sensorinf_in_db(sensor_id, rw_usr, rw_pass, db_loc):
    print("\nTesting sensor information is in the database.")
    cursor = get_rw_cursor(rw_usr, rw_pass, db_loc)
    cursor_inf = list(cursor.observatories.find({"_id": sensor_id}))[0]
    if cursor_inf:
        print("Checking sensor info in db Failed!")
        return 1
    else:
        print("Checking sensor info in db Success!")
        return 0
    

def test_insert_rawdat(sensor_id, sensor_script, rw_usr, rw_pass, db_loc):
    cursor = get_rw_cursor(rw_usr, rw_pass, db_loc)
    test_dat = {"name": "test"}
    test_fail = 0
    # Try inserting raw data into the database.
    print("\nTesting inserting raw sensor_data using script.")
    try:
        sensor_script.write_raw_dat(test_dat)
        print("Successfully written to the database!")
    except Exception as e:
        print("Failed to insert raw data into database using script.")
        print(e)
    
    raw_test_dat = list(cursor.sensorDat.find({"_id": sensor_id, "name": "test"}))[0]
    if raw_test_dat:
        print("Checking raw sensor data in db Failed!")
        test_fail = 1
    else:
        print("Checking raw sensor data in db Success!")
        test_fail = 0
    
    try:
        cursor = get_rw_cursor(rw_usr, rw_pass, db_loc)
        cursor.sensorDat.delete_one(test_dat)
    except Exception as e:
        print("Warning! Failed to delete test raw data from database.")
        print("Data", test_dat, "needs deleting manually from sensorDat!") 
        print(e)
    return test_fail
    


def test_insert_magdat(sensor_id, sensor_script, rw_usr, rw_pass, db_loc):
    cursor = get_rw_cursor(rw_usr, rw_pass, db_loc)
    test_dat = {"name": "test"}
    test_fail = 0
    # Try inserting raw data into the database.
    print("\nTesting inserting raw sensor_data using script.")
    try:
        sensor_script.write_mag_dat(test_dat)
        print("Successfully written to the database!")
    except Exception as e:
        print("Failed to insert raw data into database using script.")
        print(e)
        
    raw_test_dat = list(cursor.magnetDat.find({"_id": sensor_id, "name": "test"}))[0]
    if raw_test_dat:
        print("Checking magnetometer sensor data in db Failed!")
        test_fail = 1
    else:
        print("Checking magnetometer sensor data in db Failed!data in db Success!")
        test_fail = 0

    try:
        cursor.magnetDat.delete_one(test_dat)
    except Exception as e:
        print("Warning! Failed to delete test magnetometer data from database.")
        print("Data", test_dat, "needs deleting manually from sensorDat!")  
        print(e)
    return test_fail


def run_all_tests(sensor_id, sensor_script, rw_usr, rw_pass, db_loc=DB_LOC):
    print("Running tests for newly added sensor...")
    failed_tests = 0
    failed_tests += check_sensorinf_in_db(sensor_id, rw_usr, rw_pass, db_loc)
    failed_tests += test_insert_rawdat(sensor_id, sensor_script, rw_usr, rw_pass, db_loc)
    failed_tests += test_insert_magdat(sensor_id, sensor_script, rw_usr, rw_pass, db_loc)
    print("Total number of failed tests:", failed_tests)