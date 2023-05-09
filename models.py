from peewee import *

db = SqliteDatabase("db.sqlite3")

class Users(Model):
    firstname = CharField(max_length=30, null=True)
    lastname = CharField(max_length=30, null=True)
    username = CharField(null=True)
    uid = IntegerField(null=True)

    class Meta:
        database = db
db.connect()
db.create_tables([Users])