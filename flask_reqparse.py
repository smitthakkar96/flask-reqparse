from copy import deepcopy

import collections
import json
from flask import current_app, request, jsonify
from werkzeug.datastructures import MultiDict, FileStorage
from werkzeug import exceptions
import decimal
import six
from werkzeug.exceptions import default_exceptions, HTTPException, BadRequest
from flask import make_response, abort as flask_abort, request

class JSONHTTPException(HTTPException):
    """A base class for HTTP exceptions with ``Content-Type:
    application/json``.

    The ``description`` attribute of this class must set to a string (*not* an
    HTML string) which describes the error.

    """

    def get_body(self, environ):
        """Overrides :meth:`werkzeug.exceptions.HTTPException.get_body` to
        return the description of this error in JSON format instead of HTML.

        """
        return json.dumps(dict(description=self.get_description(environ)))

    def get_headers(self, environ):
        """Returns a list of headers including ``Content-Type:
        application/json``.

        """
        return [('Content-Type', 'application/json')]


class JSONBadRequest(JSONHTTPException, BadRequest):
    """Represents an HTTP ``400 Bad Request`` error whose body contains an
    error message in JSON format instead of HTML format (as in the superclass).

    """

    #: The description of the error which occurred as a string.
    description = (
        'The browser (or proxy) sent a request that this server could not '
        'understand.'
    )



def abort(status_code, body=None, headers={}):
    """
    Content negiate the error response.

    """

    if 'text/html' in request.headers.get("Accept", ""):
        error_cls = HTTPException
    else:
        error_cls = JSONHTTPException

    class_name = error_cls.__name__
    bases = [error_cls]
    attributes = {'code': status_code}

    if status_code in default_exceptions:
        # Mixin the Werkzeug exception
        bases.insert(0, default_exceptions[status_code])

    error_cls = type(class_name, tuple(bases), attributes)
    flask_abort(make_response(error_cls(body), status_code, headers))

    return True

class RequestParser:
    required_args = []
    def add_argument(self, name, type = None, required = False, help = None, source = None):
        if source:
            required_args.append({
                'name' : name,
                'type' : type,
                'required' : required,
                'error_message' : help,
                'source' : source
            })
        else:
            if request.method == 'GET':
                self.required_args.append({
                    'name' : name,
                    'type' : type,
                    'required' : required,
                    'error_message' : help,
                    'source' : 'args'
                })
            else:
                self.required_args.append({
                    'name' : name,
                    'type' : type,
                    'required' : required,
                    'error_message' : help,
                    'source' : 'json'
                })

    def parse_args(self):
        args = {}
        import pdb; pdb.set_trace()
        for r in self.required_args:
            try:
                if r['source'] == 'json':
                    value = request.json.get(r['name'])
                elif r['source'] == 'args':
                    value = request.json.get(r['name'])
                elif r['source'] == 'form':
                    value = request.form.get(r['name'])
                elif r['source'] == 'file':
                    value = request.files.get(r['name'])

                if value:
                    if 'type' in args:
                        args[r['name']] = args['type'](value)
                        continue
                    args[r['name']] = value
                elif r['required'] and value is None:
                    if 'error_message' in r:
                        import pdb; pdb.set_trace()
                        return abort(400, r['error_message'])
                    message = '{} must be passed as {} data'.format(r['name'], r['source'])
                    abort(400, r['error_message'])
            except KeyError:
                if 'error_message' in r:
                    return abort(400, r['error_message'])
                message = '{} must be passed as {} data'.format(r['name'], r['source'])
                abort(400, r['error_message'])
        return args