#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:41:23 2018

@author: james
"""

from pymongo import MongoClient

import json
 
# Constant for the database location.
DB_HOST="localhost"

# The database read user password (NEEDS SETTING).
READ_PASS = "readpassword"


def get_read_cursor(password=READ_PASS,
                    db_host=db_host):
    return MongoClient(db_host,
                       username="Datreader",
                       password=password,
                       authSource="mag_db")["mag_db"]
