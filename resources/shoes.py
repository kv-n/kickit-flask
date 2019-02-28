from flask import jsonify, Blueprint, request

from flask_restful import (Resource, Api, reqparse, fields, marshal, marshal_with, url_for)

import models

##define fields on our responses to the client
shoe_fields = {
    'id': fields.Integer,
    'brand': fields.String,
    'name': fields.String,
    'size': fields.Float,
    'price': fields.Integer,
    'picture': fields.String,
    'description': fields.String,
    'created_by': fields.String
}

## return shoes from db or 404
def shoe_or_404(shoe_id):
    try:
        shoe = models.Shoe.get(models.Shoe.id==shoe_id)
    except models.Shoe.DoesNotExist:
        abort(404)
    else:
        return shoe

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
        self.reqparse.add_argument(
            # what are requests need to look like
            'size',
            required = True,
            help = "No size provided",
            location = ['form', 'json']
        )
        self.reqparse.add_argument(
            # what are requests need to look like
            'price',
            required = True,
            help = "No price provided",
            location = ['form', 'json']
        )
        self.reqparse.add_argument(
            # what are requests need to look like
            'picture',
            required = True,
            help = "No picture provided",
            location = ['form', 'json']
        )
        self.reqparse.add_argument(
            # what are requests need to look like
            'description',
            required = True,
            help = "No description provided",
            location = ['form', 'json']
        )
        self.reqparse.add_argument(
            # what are requests need to look like
            'created_by',
            required = True,
            help = "No user provided",
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
        data = request.get_data()
        # print(data, 'obejctoek')
        args = self.reqparse.parse_args()
        print(args, ' hitting args in post request in shoe api')
        shoe = models.Shoe.create(brand=args['brand'], name=args['name'], size=args['size'], price=args['price'], picture=args['picture'], description=args['description'], created_by=args['created_by'])
        # print(type(shoe))
        print(shoe.__dict__, 'this is the show')
        return shoe
        
# get all shoes with id (put, delete)
class Shoe(Resource):
    def __init__(self):
        # setting up body-parser
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
        self.reqparse.add_argument(
            # what are requests need to look like
            'size',
            required = True,
            help = "No size provided",
            location = ['form', 'json']
        )
        self.reqparse.add_argument(
            # what are requests need to look like
            'price',
            required = True,
            help = "No price provided",
            location = ['form', 'json']
        )
        self.reqparse.add_argument(
            # what are requests need to look like
            'picture',
            required = True,
            help = "No picture provided",
            location = ['form', 'json']
        )
        self.reqparse.add_argument(
            # what are requests need to look like
            'description',
            required = True,
            help = "No description provided",
            location = ['form', 'json']
        )
        self.reqparse.add_argument(
            # what are requests need to look like
            'created_by',
            required = True,
            help = "No user provided",
            location = ['form', 'json']
        )
        
        # inherit from all the component properties
        super().__init__()

    @marshal_with(shoe_fields)
    def get(self, id):
        ## define a function to find our dog or send a 404
        return shoe_or_404(id)

    # @marshal_with(shoe_fields)
    # def put(self, id):
    #     print('hitting put')
    #     args = self.reqparse.parse_args()
    #     query =  models.Shoe.update(**args).where(models.Shoe.id==id)
    #     print(args)
    #     ##execute the update query
    #     query.execute()
    #     return (models.Shoe.get(models.Shoe.id==id), 200)

    def delete(self, id):
        query = models.Shoe.delete().where(models.Shoe.id==id)
        query.execute()
        return 'resource was deleted'

## the basic idea of a blueprint is that it tells our app
#  when its registered a record of the operations
# in the file to generate urls

# get all shoes with id (put, delete)
class ShoeEdit(Resource):
    def __init__(self):
        # setting up body-parser
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
        self.reqparse.add_argument(
            # what are requests need to look like
            'size',
            required = True,
            help = "No size provided",
            location = ['form', 'json']
        )
        self.reqparse.add_argument(
            # what are requests need to look like
            'price',
            required = True,
            help = "No price provided",
            location = ['form', 'json']
        )
        self.reqparse.add_argument(
            # what are requests need to look like
            'picture',
            required = True,
            help = "No picture provided",
            location = ['form', 'json']
        )
        self.reqparse.add_argument(
            # what are requests need to look like
            'description',
            required = True,
            help = "No description provided",
            location = ['form', 'json']
        )
        self.reqparse.add_argument(
            # what are requests need to look like
            'created_by',
            required = True,
            help = "No user provided",
            location = ['form', 'json']
        )
        
        # inherit from all the component properties
        super().__init__()
    

    @marshal_with(shoe_fields)
    def put(self, id):
        print(id)
        print('hitting put')
        args = self.reqparse.parse_args()
        query =  models.Shoe.update(**args).where(models.Shoe.id==id)
        print(args)
        ##execute the update query
        query.execute()
        return (models.Shoe.get(models.Shoe.id==id), 200)


## express app.use(fruitsContoller, /router)
shoes_api = Blueprint('resources.shoes', __name__)


## this gives us special methods to work with the API
api = Api(shoes_api)

api.add_resource(
    ShoeList,
    '/shoes'
)

api.add_resource(
    Shoe,
    '/shoes/<int:id>'
)

api.add_resource(
    ShoeEdit,
    '/shoes/<int:id>/edit'
)