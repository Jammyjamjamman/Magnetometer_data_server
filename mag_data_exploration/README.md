## Exploring the Frongoch farm magnetometer data.

These are the original files, used for processing the raw sensor data for frongoch farm. Working out how to process the raw data was very experimental, so it was all done in the form of jupyter notebooks.

The processing consisted of 3 stages:

1. Preprocessing the local raw data. The main preprocessing involved was converting timestamps (in various formats) into useable unix-like timestamps. The preprocessed data was then saved as yearly csv's, which is easily readable by various programs.

2. Processing the local raw data into magnetometer variameter data. This required many steps:
    * Downsampling the raw data from ~3s to 1min, by taking an average.
    * Converting the sensor reading number into a frequency/ period.
    * Splitting the data at large step changes/ time discontinuities.
    * Correcting the temperature readings.
    * Removing the temperature dependency.
    * Removing the temperature dependency from the period readings.
    * Converting the corrected period readings to magnetometer readings (in nT).
    
3. Getting data from the Hartland Observatory. This was done by using the [geomag-algorithms](https://github.com/usgs/geomag-algorithms/tree/master/geomagio) repository, provided by USGS. This can be used to retrieve Hartland magnetometer data, which could be compared with the local Frongoch-farm magnetometer data.