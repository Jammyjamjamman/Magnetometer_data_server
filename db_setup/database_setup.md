## Setting up the MongoDB

### 1. Download and install [MongoDB v4](https://www.mongodb.com/download-center?jmp=nav#community)


### 2. Create admin account.
This account can create users and add/ revoke user roles. Creating the admin account requires starting the database without authentication enabled. To do this, run in a terminal:

```
mongod --port 27017 --dbpath /path/to/db
```

where `/path/to/db` is where you want to store the database data. I used a directory supplied in this github, which is:

```
/path/to/Magnetometer_data_server/db_data/db
```

Next, in another terminal, connect to the database:

```
mongo --port 27017
```

This will connect you to your database's shell. In the shell create the administrator account. This will be used to create all other accounts (remember to change the password, under pwd!).

```
use admin

db.createUser(
    {
        user: "Administrator",
        // Change this password!
        pwd: "adminpassword",
        roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
    }
)

exit
```

After creating the admin account and disconnecting, restart the database and enable authentication:

```
mongod --auth --dbpath /path/to/db_data/db/ --shutdown

mongod --auth --dbpath /path/to/Magnetometer_data_server/db_data/db/
```

See [Enable Auth](https://docs.mongodb.com/manual/tutorial/enable-authentication/) for more info.



### 3. Create the database and configure users.

Log in as administrator:

```
mongo -u Administrator --authenticationDatabase "admin" mongodb://localhost
```

and enter the password you created for the administrator account.
Create a magnetometer database called "mag_db":

```
use mag_db
```

Create custom roles for the database. These will be used by users trying to insert magnetometer readings into the database and by users trying to access the data.

Create a role for inserting and updating observatory/ sensor information into the database:

```
db.createRole(
    {
        role: "readWriteObservatories",
        privileges: [
            { resource: { db: "mag_db", collection: "observatories"}, actions: ["find", "update", "insert", "remove"] },
        ],
        roles: []
    }
)
```

Create a role for inserting raw sensor data into the database. This is data that needs processing before magnetometer readings are.

```
db.createRole(
    {
        role: "writeSensorDat",
        privileges: [
            { resource: { db: "mag_db", collection: "sensorDat"}, actions: ["find", "insert"] },
        ],
        roles: []
    }
)
```

Create a role for inserting magnetometer data into the database. This is data that has already been processed into actual magnetic field readings.

```
db.createRole(
    {
        role: "writeMagnetDat",
        privileges: [
            { resource: { db: "mag_db", collection: "magnetDat"}, actions: ["find", "insert"] },
        ],
        roles: []
    }
)
```


### 4. Create users.

These are the users who will interact directly with the database. It is recommended to keep the usernames the same, as these are known users by other python scripts. However, the passwords should be changed.
Create the user that manages observatories:

```
db.createUser(
    {
        user: "Obsmanager",
        // Change this password!
        pwd: "obspassword",
        roles: [ { role: "readWriteObservatories", db: "mag_db" } ]
    }
)
```

Create the user that writes raw sensor data to the database:

```
db.createUser(
    {
        user: "Sensorwriter",
        // Change this password!
        pwd: "senpassword",
        roles: [ { role: "writeSensorDat", db: "mag_db" } ]
    }
)
```

Create the user that writes processed magnetometer data to the database:

```
db.createUser(
    {
        user: "Magnetwriter",
        // Change this password!
        pwd: "magpassword",
        roles: [ { role: "writeMagnetDat", db: "mag_db" } ]
    }
)
```

Create the user that can read the entire database. This user is used by the server to get data from the database:

```
db.createUser(
    {
        user: "Datreader",
        // Change this password!
        pwd: "readpassword",
        roles: [ { role: "read", db: "mag_db" } ]
    }
)
```

Create a user that can read and write to the entire database. This user can be used to correct any mistakes made in the database:
```
db.createUser(
    {
        user: "Readwriter",
        // Change this password.
        pwd: "rwpassword",
        roles: [ { role: "readWrite", db: "mag_db" } ]
    }
)
```

** Note: The Administrator account and the Readwriter account should only be known by a few people and not accessible to the server, sensors or anything else. **


### 5. Create indexes (use Datreader/Readwriter account). Since we are dealing with timeseries data, the data needs to be accessible and sorted based on time. Therefore, index time in the raw sensor.

```
db.sensorDat.createIndex({ "time": 1 })
db.magnetDat.createIndex({ "time": 1 })
```

### 6. Setup the relevant python scripts with database usernames and passwords.

Open the Jupyter notebook [Encrypt_DB_Passwords](file://Encrypt_DB_passwords.ipynb) to encrypt the passwords (this needs to be done in a jupyter environment, in a web browser. See [Installing Jupyter Notebooks](https://jupyter.readthedocs.io/en/latest/projects/content-projects.html).)
