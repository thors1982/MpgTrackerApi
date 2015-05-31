from bson import json_util
from flask_restful import Resource, Api, reqparse, abort
from common.Util import Util
from resources import app, api, mongo

#Validation
userparser = reqparse.RequestParser()
userparser.add_argument('firstname', type=str)
userparser.add_argument('lastname', type=str)

class UserDetail(Resource):
	def get(self, username):
		user = mongo.db.users.find_one_or_404({"username": username})
		return json_util.dumps(user, default=json_util.default)
	
	def put(self, username):
		user = mongo.db.users.find_one_or_404({"username": username})
		
		usernameparser = reqparse.RequestParser(trim=True)
		usernameparser.add_argument('username', type=str)
		usernameparser.add_argument('firstname', type=str)
		usernameparser.add_argument('lastname', type=str)
		args = usernameparser.parse_args(strict=True)
		
		if args['firstname']:
			user['firstname'] = args['firstname']
			
		if args['lastname']:
			user['lastname'] = args['lastname']
		
		mongo.db.users.update({"username": username}, user)
		
		return '', 204
		
	
	def delete(self, username):
		mongo.db.users.find_one_or_404({"username": username})
		mongo.db.users.remove({"username": username})
		return '', 204
		

api.add_resource(UserDetail, '/users/<string:username>')