from bson import json_util
from flask_restful import Resource, Api, reqparse, abort
from common.Util import Util
from resources import app, api, mongo

class UsersCollection(Resource):
	def get(self):
		query = mongo.db.users.find()
		list = [json_util.dumps(doc, default=json_util.default) for doc in query]
		return {'List': list}
	
	def post(self):
		usernameparser = reqparse.RequestParser(trim=True)
		usernameparser.add_argument('username', type=str, required=True)
		usernameparser.add_argument('firstname', type=str)
		usernameparser.add_argument('lastname', type=str)
		args = usernameparser.parse_args(strict=True)
		
		userid =  mongo.db.users.insert(args)
		return '', 201

api.add_resource(UsersCollection, '/users')