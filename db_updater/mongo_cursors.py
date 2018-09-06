#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:41:23 2018

@author: james
"""

from pymongo import MongoClient

from cryptography.fernet import Fernet
import json
 
# Constants for accessing the database usernames and passwords (NEED SETTING).
PASS_LOC = "access.crypt"
KEY = b'bZ54iqDolhe8n-UBJ8wCwOgN61a9_Ef_TUX7HUB5LIE='
OBSW_USR = "Obsmanager"
SENW_USR = "Sensorwriter"
MAGW_USR = "Magnetwriter"

# Constant for the database web location.
DB_HOST = "localhost"


def get_passwords(key, pass_loc):
    f = Fernet(key)
    with open(pass_loc, 'rb') as cr_file:
        return json.loads(f.decrypt(cr_file.read()).decode("utf-8"))


def get_obs_writer(key=KEY,
                   usr=OBSW_USR,
                   pass_loc=PASS_LOC,
                   db_host=DB_HOST):
    password_dict = get_passwords(key, pass_loc)
    return MongoClient(db_host,
                       username=usr,
                       password=password_dict[usr],
                       authSource="mag_db")["mag_db"]["observatories"]