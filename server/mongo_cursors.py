#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:41:23 2018

@author: james
"""

from pymongo import MongoClient
 
# Constant for the database location.
DB_HOST="localhost"

# The database read user and password (NEEDS SETTING).
READ_USR = "Datreader"
READ_PASS = "readpassword"


def get_read_cursor(usr=READ_USR,
                    password=READ_PASS,
                    db_host=DB_HOST):
    """Returns a cursor for reading the mongo database.
    
    Returns:
        cursor: A cursor for reading the magnetometer database.
    """
    return MongoClient(db_host,
                       username=usr,
                       password=password,
                       authSource="mag_db")["mag_db"]
