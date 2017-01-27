# flask_reqparse

flask_reqparse is a simple wrapper around flask request module that helps to parse args efficently

Request Parsing
===============

Installation
------------

To install flask_reqparse use  
````pip install flask_reqparse````

To parse the arguments with flask_reqparse, here is an example

``` python
from flask import Flask, jsonify
from flask_reqparse import RequestParser

parser = RequestParser()

app = Flask(__name__)

@app.route('/api/json', methods=['POST'])
@parser.validate_arguments([
    {
        'name' : "name",
        'required' : True,
        'source' : 'args',
        'help' : 'Name cannot be null'
    }
])
def json_demo(args):
    return jsonify({"response" : "hello " + args['name']})

@app.route('/api/args_demo')
@parser.validate_arguments([
    {
        'name' : "name",
        'required' : True,
        'type' : list
    }
])
def args_demo(args):
    return jsonify({"response" : args['name']})


if __name__ == '__main__':
    app.run(debug=True)
```


Inspired from Flask-Restful Request Parser
