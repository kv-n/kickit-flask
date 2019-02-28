import json

from flask import jsonify, Blueprint, abort, make_response

from flask_restful import (Resource, Api, reqparse,
                               inputs, fields, marshal,
                               marshal_with, url_for)

from flask_login import login_user, logout_user, login_required, current_user
import models
from flask_bcrypt import check_password_hash
from peewee import *

user_fields = {
    'username': fields.String,
    'email': fields.String,
    'password': fields.String,
}


class UserList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='No username provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'email',
            required=True,
            help='No email provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'password',
            required=True,
            help='No password provided',
            location=['form', 'json']
        )
        super().__init__()


    def post(self):
        args = self.reqparse.parse_args()
        # if args['password'] == args['password']:
        print(args, ' this is args')
        user = models.User.create_user(username=args['username'], email=args['email'], password=args['password'])
        login_user(user)
        print(user)
        # print(user)
        return marshal(user, user_fields), 201
        return make_response(
            json.dumps({
                'error': 'Password and password verification do not match'
            }), 400)


class UserLogin(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='No username provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'email',
            required=True,
            help='No email provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'password',
            required=True,
            help='No password provided',
            location=['form', 'json']
        )
        super().__init__()

    def post(self):
        args = self.reqparse.parse_args()
        print(args['username'])
        try:
            logged_user = models.User.get(models.User.username == args['username'])
        except:
            logged_user = False
    
        if logged_user and check_password_hash(logged_user.password, args['password']):
            login_user(logged_user)
            print(current_user)
            print('current_user')
            return marshal(logged_user.get(), user_fields)
        else:
            return 'Youre email or password doesnt match'

def logout():
    # destroying our session
    logout_user()
    flash('youve been logged out', 'success')
    return redirect(url_for('index'))

users_api = Blueprint('resources.users', __name__)
api = Api(users_api)

api.add_resource(
    UserList,
    '/users',
    endpoint='users'
)

api.add_resource(
    UserLogin,
    '/users/login',
    endpoint='userslogin'
)