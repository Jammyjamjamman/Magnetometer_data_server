## Running the Server

Before starting the server, make sure the database reader username, password and database location is set in `mongo_cursors.py`.

To start the server, run server.py:

```sh
python server.py
```

Note that the server is set in debug mode. To switch off debug mode, in `server.py`, change the lines:
```py
if __name__ == "__main__":
    app.run(debug=True)
```

to:

```py
if __name__ == "__main__":
    app.run(debug=False)
```
