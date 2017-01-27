import sys

from flask import Flask, jsonify

sys.path.insert(0, '../')
from flask_reqparse import RequestParser



app = Flask(__name__)

@app.route('/api/json', methods=['POST'])
def json_demo():
    parser = RequestParser()
    parser.add_argument('name', required=True)
    parser.add_argument('email', required=True, help="email is required")
    args = parser.parse_args()
    print(args['name'])
    print(args['email'])
    return jsonify({"response" : "success"})

if __name__ == '__main__':
    app.run()
