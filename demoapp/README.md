# Demo app
Simple demo http server which is needed to run the examples from other suites.
Demo server has a flask as a dependency:
```
    pip install flask
```

# Start demo app
To start the demo server, give command:
```
    python server.py
```

To start the another demo server based on flask, give command:
```
    FLASK_APP=flask_app.py FLASK_ENV=development FLASK_DEBUG=1  flask run
```




