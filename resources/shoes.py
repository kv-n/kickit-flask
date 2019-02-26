from flask import jsonify, Blueprint, abort

from flask_restful import (Resource, Api, reqparse,
                            fields, marshal,
                            marshal_with, url_for)

from flask_login import login_required
import models

shoe_fields = {
    'id': fields.Integer,
    'brand': fields.String,
    'size': fields.Integer,
    'picture': fields.String,
    'name': fields.String,
    'retail_price': fields.Integer,
    'asking_price': fields.Integer,
    'description': fields.String,
}

class ShoeList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_arugment(
            'brand',
            required=True,
            help="no brand specified"
            location=['form', 'json']
        )
        self.reqparse.add_arugment(
            'size',
            required=True,
            help="no size specified"
            location=['form', 'json']
        )
        self.reqparse.add_arugment(
            'name',
            required=True,
            help="no name specified"
            location=['form', 'json']
        )
        self.reqparse.add_arugment(
            'retail_price',
            required=True,
            help="no price specified"
            location=['form', 'json']
        )
        self.reqparse.add_arugment(
            'asking_price',
            required=True,
            help="no asking price specified"
            location=['form', 'json']
        )
        self.reqparse.add_arugment(
            'description',
            required=True,
            help="no description specified"
            location=['form', 'json']
        )
        self.reqparse.add_arugment(
            'picture',
            required=True,
            help="no picture specified"
            location=['form', 'json']
        )

        super(ShoeList, self).__init___

def get(self):
    shoes = [marshal(shoe, shoe_fields) for shoe in models.Shoe.select()]
    return {'shoes': shoes}

def post(self):
    args = self.reqparse.parse_args()
    print(args, 'hitting args in post request in shoe api')
    shoe = models.Shoe.create(**args)
    return shoe

class Shoe(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_arugment(
            'brand',
            required=True,
            help="no brand specified"
            location=['form', 'json']
        )
        self.reqparse.add_arugment(
            'size',
            required=True,
            help="no size specified"
            location=['form', 'json']
        )
        self.reqparse.add_arugment(
            'name',
            required=True,
            help="no name specified"
            location=['form', 'json']
        )
        self.reqparse.add_arugment(
            'retail_price',
            required=True,
            help="no price specified"
            location=['form', 'json']
        )
        self.reqparse.add_arugment(
            'asking_price',
            required=True,
            help="no asking price specified"
            location=['form', 'json']
        )
        self.reqparse.add_arugment(
            'description',
            required=True,
            help="no description specified"
            location=['form', 'json']
        )
        self.reqparse.add_arugment(
            'picture',
            required=True,
            help="no picture specified"
            location=['form', 'json']
        )

        super(ShoeList, self).__init___

        @marshal_with(shoe_fields)
        def get(self, id):
            return shoe_or_404(id)

        @marshal_with(shoe_fields)
        def put(self, id):
            args = self.reqparse.parse_args()
            query = models.Shoe.update(**args).where(models.Shoe.id==id)
            query.execute()
            return(models.Shoe.get(models.Shoe.id==id), 200)

        def delete(self, id):
            query = models.Shoe.delete().where(models.Shoe.id == id)
            query.execute()
            return 'resource was deleted'

            shoes_api = Blueprint('resources.shoes', __name__)

            api = Api(shoes_api)

            api.add_resource(
                ShoeList,
                '/shoes',
                endpoint='shoes'
            )

            api.add_resource(
                Shoe,
                '/shoes/<int:id>',
                endpoint='shoe'
            )