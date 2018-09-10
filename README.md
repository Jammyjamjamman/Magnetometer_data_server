# Magnetometer_data_server
This repository provides python code and Jupyter notebooks for processing historic magnetometer sensor readings retrieved at Frongoch Farm, Aberystwyth University and for extracting magnetometer readings.

Prototype server code and a jupyter notebook for making the magnetometer data from Frongoch Farm and the Hartland observatory is also available.

This code is for my Masters Project for Aberystwyth University.

## Retrieving and Visualising Data from Frongoch Magnetometer
See the code in [client_interface](client_interface).

## Exploring and Processing the Original Frongoch Magnetometer
See the code in [mag_data_exploration](mag_data_exploration).

## Setting up a Server with Magnetometer Data from Frongoch and Hartland
Cloning this repository is recommended for setting up a server. There are 3 steps to setting up the Server:
1. Setup and start the Mongo database. Instructions: [db_setup](db_setup)
2. Load data into the database. Instructions: [db_updater](db_updater)
3. Setup the server. Instructions: [server](server)

Known problems/ TODO:
* Data from sensors is directly sent to the database. This potentially poses a security risk.
* The server cannot update sensor data automatically.
* Setting up the server is clunky and requires copying files and passwords around.
* Adding sensors to the database is clunky.
* Deleting data can only be done easily from the Mongo shell.
* The webpage for retrieving data is only the Bare minimum. You cannot see the data you are about to retrieve, or if you will retrieve any data.
* Retrieving raw data is very slow.

## Requirements
### For Everyone
* Python (Anaconda Python 3 Recommended)
* numpy
* scipy
* scikit-learn
* pandas
* jupyter
* matplotlib
* geomag-aglorithms

### Raw Data Processing
* PyChange
* [igrf12](https://github.com/scivision/igrf12)

### Setting up the Database or inserting into Database
* pymongo
* cryptography

### Setting up the Server
* pymongo
* cryptography
* flask
* flask-cors
