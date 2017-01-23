# flask_reqparse

flask_reqparse is a simple wrapper around flask request module that helps to parse args efficently

Request Parsing
===============

Basic Arguments
---------------

Here's a simple example of the request parser. It looks for two arguments in
the :attr:`flask.Request.values` dict: an integer and a string ::

    from flask_restful import reqparse

    parser = reqparse.RequestParser()
    parser.add_argument('rate', type=int, help='Rate cannot be converted')
    parser.add_argument('name')
    args = parser.parse_args()

.. note ::

    The default argument type is a unicode string. This will be ``str`` in
    python3 and ``unicode`` in python2.

If you specify the ``help`` value, it will be rendered as the error message
when a type error is raised while parsing it.  If you do not specify a help
message, the default behavior is to return the message from the type error
itself. See :ref:`error-messages` for more details.

By default, arguments are **not** required.  Also, arguments supplied in the
request that are not part of the RequestParser will be ignored.

Also note: Arguments declared in your request parser but not set in
the request itself will default to ``None``.

Required Arguments
------------------

To require a value be passed for an argument, just add ``required=True`` to
the call to :meth:`~reqparse.RequestParser.add_argument`. ::

    parser.add_argument('name', required=True,
    help="Name cannot be blank!")

Argument Locations
------------------

By default, the :class:`~reqparse.RequestParser` tries to parse values from
:attr:`flask.Request.values`, and :attr:`flask.Request.json`.

Use the ``location`` argument to :meth:`~reqparse.RequestParser.add_argument`
to specify alternate locations to pull the values from. Any variable on the
:class:`flask.Request` can be used. For example: ::

    # Look only in the POST body
    parser.add_argument('name', type=int, location='form')

    # Look only in the querystring
    parser.add_argument('PageSize', type=int, location='args')

    # Look only in json
    parser.add_argument('picture', type=str, location='json')

    # Look only in Form
    parser.add_argument('picture', type=str, location='form')


Inspired from Flask-Restful Request Parser
