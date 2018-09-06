#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:41:23 2018

@author: james
"""

from pymongo import MongoClient

from cryptography.fernet import Fernet
import json
 
# Constants for accessing the database passwords (NEED SETTING).
PASS_LOC = "access.crypt"
KEY = b'bZ54iqDolhe8n-UBJ8wCwOgN61a9_Ef_TUX7HUB5LIE='

# Constant for the database web location.
DB_HOST = "localhost"

def get_passwords(key=KEY, pass_loc):
    f = Fernet(key)
    with open(pass_loc, 'rb') as cr_file:
        return json.loads(f.decrypt(cr_file.read()).decode("utf-8"))

def get_obs_writer(key=KEY,
                      pass_loc=pass_loc,
                      db_host=db_host):
    password_dict = get_passwords(key, pass_loc)
    return MongoClient("localhost",
                       username="Obsmanager",
                       password=password_dict["Obsmanager"],
                       authSource="mag_db")["mag_db"]["observatories"]