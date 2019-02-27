import datetime

from peewee import *
from flask_bcrypt import generate_password_hash
from flask_login import UserMixin

import config
DATABASE = SqliteDatabase('shoesdatabase.sqlite')


class User(UserMixin, Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE
    
#     # def get_stream(self):
#     #     return Shoe.select().where(
#     #         (Shoe.user == self)
#     #     )

    @classmethod
    def create_user(cls, username, email, password):
        email = email.lower()
        try:
            cls.select().where(
                (cls.email==email)
            ).get()
        except cls.DoesNotExist:
            user = cls(username=username, email=email)
            user.password = generate_password_hash(password)
            user.save()
            return user
        else:
            raise Exception("User with that email or username already Exists")

class Shoe(Model):
    brand = CharField()
    name = CharField()
    size = CharField()
    price = CharField()
    picture = CharField(null=True)
    description = CharField()
    created_by = ForeignKeyField(User, backref='shoe_user')
    

    created_at = DateTimeField(default=datetime.datetime.now)

    # user = ForeignKeyField(
    #     model=User,
    #     backref='shoe'
    #     )
    # content = TextField()

    class Meta:
        # class instrcutions on how to build class, what database the class is communcating with
        database = DATABASE

class Kickit(Model):
    user_username = ForeignKeyField(User, backref='users')
    shoe_id = ForeignKeyField(Shoe, backref='shoes')

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Shoe], safe=True)
    DATABASE.close()

