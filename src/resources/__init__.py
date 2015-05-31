from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
#from pymongo import MongoClient
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
app.debug = True
api = Api(app)

mongo = PyMongo(app)

import UsersCollection
import UserDetail