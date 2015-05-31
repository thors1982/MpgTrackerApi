'''
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
#from pymongo import MongoClient
from flask.ext.pymongo import PyMongo
from resources.userscollection import UsersCollection
from resources.userdetail import UserDetail

app = Flask(__name__)
app.debug = True
api = Api(app)

mongo = PyMongo(app)

users = {
	'jean9' : {'firstname': 'Jeannine', 'lastname': 'Tondreau'},
	'nstark': {'firstname': 'Nick', 'lastname': 'Stark'},
}

#Rest Controllers
class ApiDocumentation(Resource):
	def get(self):
		return 'Api documentation'

#Routing
api.add_resource(ApiDocumentation, '/')
api.add_resource(UsersCollection, '/users')
api.add_resource(UserDetail, '/users/<string:username>')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

'''

from resources import app
app.run(host='0.0.0.0')