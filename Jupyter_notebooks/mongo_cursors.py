#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:41:23 2018

@author: james
"""

from pymongo import MongoClient

from cryptography.fernet import Fernet
import json
 
pass_loc="access.crypt"
db_host="localhost"


def get_passwords(key, pass_loc):
    f = Fernet(key)
    with open(pass_loc, 'rb') as cr_file:
        return json.loads(f.decrypt(cr_file.read()).decode("utf-8"))


def get_read_cursor(key=b'bZ54iqDolhe8n-UBJ8wCwOgN61a9_Ef_TUX7HUB5LIE=',
                    pass_loc=pass_loc,
                    db_host=db_host):
    password_dict = get_passwords(key, pass_loc)
    return MongoClient(db_host,
                       username="Datreader",
                       password=password_dict["Datreader"],
                       authSource="mag_db")["mag_db"]