from flask import jsonify, Blueprint

from flask_restful import (Resource, Api, reqparse, fields, marshal, marshal_with, url_for)

import models

##define fields on our responses to the client
shoe_fields = {
    'id': fields.Integer,
    'brand': fields.String,
    'name': fields.String,
}

## return shoes from db or 404
def shoe_or_404(shoe_id):
    try:
        shoe = models.Shoe.get(models.Shoe.id==shoe_id)
    except models.Shoe.DoesNotExist:
        abort(404)
    else:
        return dog

# Resource gives us http methods (get, post, put)
# get all dogs or create dog
class ShoeList(Resource):
    def __init__(self):
        # setting up body-parser
        print(self)
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            # what are requests need to look like
            'brand',
            required = True,
            help = "No shoe name provided",
            location = ['form', 'json']
        )
        self.reqparse.add_argument(
            # what are requests need to look like
            'name',
            required = True,
            help = "No name provided",
            location = ['form', 'json']
        )
        # inherit from all the component properties
        super().__init__()

    def get(self):
        shoes = [marshal(shoe, shoe_fields) for shoe in models.Shoe.select()]
        return {'shoes': shoes}

    @marshal_with(shoe_fields)
    def post(self):
        # dictionary of our arugements
        print('this is the postasdfasdfadsf')
        args = self.reqparse.parse_args()
        print(args, ' hitting args in post request in shoe api')
        shoe = models.Shoe.create(brand=args['brand'], name=args['name'])
        print(type(shoe))
        print(shoe.__dict__)
        return shoe, 201
        
# get all shoes with id (put, delete)
class Shoe(Resource):
    @marshal_with(shoe_fields)
    def get(self, id):
        ## define a function to find our dog or send a 404
        return shoe_or_404(id)

    def put(self, id):
        return jsonify({'brand':'nike'})

    def delete(self, id):
        return jsonify({'brand':'nike'})

## the basic idea of a blueprint is that it tells our app
#  when its registered a record of the operations
# in the file to generate urls

## express app.use(fruitsContoller, /router)
shoes_api = Blueprint('resources.shoes', __name__)


## this gives us special methods to work with the API
api = Api(shoes_api)

api.add_resource(
    ShoeList,
    '/shoes',
    endpoint = 'shoes'
)

api.add_resource(
    Shoe,
    '/shoes/<int:id>',
    endpoint = 'shoe'
)