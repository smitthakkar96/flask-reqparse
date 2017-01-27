
"""
flask-reqparse
-------------
flask-reqparse a request parser for parse apps
"""
from setuptools import setup


setup(
    name='flask-reqparse',
    version='2.0.1',
    license='BSD',
    author='smit thakkar',
    author_email='smitthakkar96@gmail.com',
    description='flask_reqparse is a simple wrapper around flask request module that helps to parse args efficently.',
    long_description=__doc__,
    py_modules=['flask_reqparse'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
