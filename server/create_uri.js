var rawDatURL = "http://localhost:5000/raw-dat";
var magDatURL = "http://localhost:5000/mag-dat";
var sensors = {};
var mintime = null;
var maxtime = null;

var downloadURI;

document.addEventListener("DOMContentLoaded", function(event) {
    
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        var sensor_select_txt="";
        if (this.readyState == 4 && this.status == 200) {
            sensors = JSON.parse(this.responseText).reduce(function(map, sensor) {
                                                                    var id = sensor._id;
                                                                    delete sensor._id
                                                                    map[id] = sensor;
                                                                    return map; }, {});
            Object.keys(sensors).forEach(function(key,index) {
                                                        sensor_select_txt += '<option value=' + key + "><b>" + sensors[key].name + "</b><br>";
                                                    }); 

            sensor_selection.innerHTML = sensor_select_txt;
            sensor_selection.value = Object.keys(sensors)[0]
            sensor_select(sensor_selection.value);
            get_start();
            get_end();
            updateURI();
        }
    };

    xmlhttp.open("GET", "http://localhost:5000/available-sensors", true);
    xmlhttp.send();
} )


function updateURI() {
    if (raw.checked) {
        downloadURI = rawDatURL;
    }
    else {
        downloadURI = magDatURL;
    }
    
    downloadURI += "?sensor_id=" + sensor_selection.value;
    
    if (mintime != null) {
        downloadURI += "&starttime=" + mintime.getTime()/1000;
    }
    
    if (maxtime != null) {
        downloadURI += "&endtime=" + maxtime.getTime()/1000;
    }
    
    uri_link.innerHTML = "<a href=" + downloadURI + ">" + '<button type="button">download</button><br><br>'
    uri_link.innerHTML += "Or use the following URI: " 
    uri_link.innerHTML += "<code>" + downloadURI + "</code>";
}


function sensor_select(sensor_id) {
    var chosen_sensor = sensors[sensor_id]
    var info_txt = "<table border='1'>"
    Object.keys(chosen_sensor).forEach(function(key,index) {
                                                        info_txt += "<tr><td>" + key + "</td><td>" + chosen_sensor[key] + "</td></tr>";
                                                    });
    info_txt += "</table>";
    sensor_info.innerHTML = info_txt;
    
}


function get_start() {
    if ((startdate.value === null) || (startdate.value == "") || (starttime.value === null) || (starttime.value == "")) {
        mintime = null;
    }
    else {
        mintime = new Date(startdate.value + " " + starttime.value);
    }
    check_endtime_gr_starttime()
}


function get_end() {
    if ((enddate.value === null) || (enddate.value == "") || (endtime.value === null) || (endtime.value == "")) {
        maxtime = null;
    }
    else {
        maxtime = new Date(enddate.value + " " + endtime.value);
    }
    check_endtime_gr_starttime();
}


function check_endtime_gr_starttime() {
    if ((mintime !== null) && (maxtime !== null) && (maxtime <= mintime)) {
        warnings.innerHTML = "Warning: End time not included in query as end time should not be less than start time!";
        maxtime = null;
    }
    else {
        warnings.innerHTML = "";
    }
}
