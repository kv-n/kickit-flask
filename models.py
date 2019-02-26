import datetime

from peewee import *

DATABASE = SqliteDatabase('shoesdatabase.sqlite')

class Shoe(Model):
    brand = CharField()
    name = CharField()
    size = CharField()
    price= CharField()
    picture = CharField()
    description = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        # class instrcutions on how to build class, what database the class is communcating with
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Shoe], safe=True)
    DATABASE.close()

