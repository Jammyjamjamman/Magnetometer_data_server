<!--
The readmes are stored as markdown files, for compatibility with github. 
It is recommended to read this readme at https://github.com/Jammyjamjamman/Magnetometer_data_server.
-->

# Magnetometer_data_server
This repository provides python code and Jupyter notebooks for processing historic magnetometer sensor readings retrieved at Frongoch Farm, Aberystwyth University and for extracting magnetometer readings.

Prototype server code and a jupyter notebook for making the magnetometer data from Frongoch Farm and the Hartland observatory is also available.

This code is for my Masters Project for Aberystwyth University.

## Visualising Data from Frongoch Magnetometer and other UK Magnetometers, from a server like the one on this github:
See the code in [client_interface](client_interface).

## Exploring and Processing the Original Frongoch Magnetometer Data:
See the code in [mag_data_exploration](mag_data_exploration).

## Setting up a Server with Magnetometer Data from Frongoch, Hartland and Eskdalemuir:
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
* io
* [geomagio](https://github.com/usgs/geomag-algorithms)

### Frongoch Farm Raw Data Analysis and Processing

* [cpDetect](https://github.com/choderalab/cpdetect)
* [igrf12](https://github.com/scivision/igrf12)

### Setting up the Database or inserting into Database
* pymongo
* cryptography

### Setting up the Server
* pymongo
* cryptography
* flask
* flask-cors

The results presented in this github rely on the data collected at Hartland. We thank the British Geological Survey, for supporting its operation and INTERMAGNET for promoting high standards of magnetic observatory practice (www.intermagnet.org).

The results presented in this github rely on the data collected at Eskdalemuir. We thank the British Geological Survey, for supporting its operation and INTERMAGNET for promoting high standards of magnetic observatory practice (www.intermagnet.org).
