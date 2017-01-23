# flask_reqparse

flask_reqparse is a simple wrapper around flask request module that helps to parse args efficently

## Example
``` python
from flask import flask
from flask_reqparse import RequestParser

@app.route('/auth/demo', methods = ['POST'])
def demo():
    parser = RequestParser()
    parser.add_argument('rate', type=int, required = True, help='Rate cannot be converted')
    parser.add_argument('name', type=str, required = True, help='Rate cannot be converted', source = 'args')
    args = parser.parse_args()
    return jsonify({"response" : "success"})
```

Arguments
    - Name of parameter
    - type (named param), optional paramter. The type in which the paramter is to be expeted. RequestParser will convert to specified type. Supported types:
        - int
        - str
        - float
        - dict
        - list
    - required is by default is False, if set to true then it will check if the paramter is passed to api if not will return 404 with the help message.
    - Help is an optional message which is used when required is set to true
    - source is default request.json for post and request.args for get. The name of the source must be passed as string. Supported sources are as follows:
        - json
        - args
        - files
        - form

