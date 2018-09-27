## Adding Data to the Database

After setting up the database, magnetometer sensor data needs adding to it. This consists of 2 steps:
1. Adding the sensor information to the database, including its ID and location details (and any other details the user wishes to add).
2. Adding the data from sensors magnetometers.

### Loading sensor information.

[Setup_Sensors.ipynb](Setup_Sensors.ipynb) Jupyter notebook goes through the steps of loading Observatory metadata from [Frongoch Farm](http://www.coflein.gov.uk/en/site/420288/details/frongoch-experimental-farm), [Hartland](http://geomag.bgs.ac.uk/operations/hartland.html) and [Eskdalemuir](http://geomag.bgs.ac.uk/operations/eskdale.html). Frongoch Farm information is also present in the [frongoch_sensor_details.json](frongoch_sensor_details.json). Information obtained about these observatories were obtained from their corresponding website.

Alternatively, sensor information can be loaded by the python function `add_sensor()` in the script [add_sensor.py](add_sensor.py). The function requires 4 arguments: a sensor identifier, the sensor latitude, lognitude, elevation and the coordinate system the sensor uses when recording magnetometer readings (see [XYZ Algorithm](https://github.com/usgs/geomag-algorithms/blob/master/docs/algorithms/XYZ.md) ).

After adding a sensor to the database, a new script called `XXX_dat_insert.py` will be generated. This script can be used to insert raw and geomagnetic data into the database.

### Loading Frongoch Farm magnetometer data.

Frongoch farm preprocessed and processed sensor data can be added to the database using [Load_Frongoch_Readings_to_DB.ipynb](Load_Frongoch_Readings_to_DB.ipynb). This notebook processes all the Frongoch Farm data, using techniques discovered in [mag_data_exploration](../mag_data_exploration). The data is then loaded to the database using [add_sensor.py](add_sensor.py).

### Loading Hartland and Eskdalemuir geomagnetic readings to the database.

[Load_HAD_ESK_Data_to_DB.ipynb](Load_HAD_ESK_Data_to_DB.ipynb) can be used to load data from Hartland and Eskdalemuir. The data must be manually obtained from [BGS](http://www.wdc.bgs.ac.uk/dataportal/) as `.json` and from [INTERMAGNET](http://www.intermagnet.org/index-eng.php) as IAGA2002 `.min` files.
