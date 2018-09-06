#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:41:23 2018

@author: james
"""

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


def encrypt_password_dict(passwords, key, crypt_file = "access.crypt"):
    """
    Encrypt a dictionary of passwords, using this function.
    """
    f = Fernet(key)
    token = f.encrypt(bytes(json.dumps(password_dict), "utf-8"))
    with open(crypt_file, 'wb') as cr_file:
        cr_file.write(token)


if __name__ == "__main__":
    # Set these passwords to the passwords you chose!
    password_dict = {"Obsmanager": "obspassword",
                     "Sensorwriter": "senpassword",
                     "Magnetwriter": "magpassword"}
    
    # Keep this safe!
    key = b'bZ54iqDolhe8n-UBJ8wCwOgN61a9_Ef_TUX7HUB5LIE='#Fernet.generate_key()
    print("The key is:", key)
    
    # Encrypt the passwords.
    encrypt_password_dict(password_dict, key)