import sys

from flask import Flask, jsonify

sys.path.insert(0, '../')
from flask_reqparse import RequestParser

parser = RequestParser()

app = Flask(__name__)

@app.route('/api/json', methods=['POST'])
@parser.validate_arguments([
    {
        'name' : "name",
        'required' : True,
        'source' : 'args'
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
