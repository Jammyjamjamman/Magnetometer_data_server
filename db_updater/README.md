## Adding Data to the Database

After setting up the database, magnetometer sensor data needs adding to it. This consists of 2 steps:
1. Adding the sensor information to the database, including its ID and location details (and any other details the user wishes to add).
2. Adding the data from sensors magnetometers.

### Loading sensor information.

Sensor details can be loaded, by opening [Load_Sensorinfo_to_DB.ipynb](Load_Sensorinfo_to_DB.ipynb) or by the python function `add_sensor()` in the script `add_sensor.py`. The function requires 4 arguments: a sensor identifier, the sensor latitude, lognitude, elevation and the coordinate system it uses when recording magnetometer readings (see [XYZ Algorithm](https://github.com/usgs/geomag-algorithms/blob/master/docs/algorithms/XYZ.md). [Load_Sensorinfo_to_DB.ipynb](Load_Sensorinfo_to_DB.ipynb) will also go through loading the magnetometer information and data from the [Hartland](http://geomag.bgs.ac.uk/operations/hartland.html) observatory.

After adding a sensor to the database, a new script, for that sensor to upload to the database, will be generated.

### Loading sensor data.

Frongoch farm preprocessed and processed sensor data can be added to the database using [Load_Frongoch_Sensordat_to_DB.ipynb](Load_Frongoch_Sensordat_to_DB.ipynb).
