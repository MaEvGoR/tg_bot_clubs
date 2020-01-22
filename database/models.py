from mongoengine import *
connect('test_db')


class User(Document):
    u_id = IntField(required=True, unique=True)
    name = StringField(required=False, max_length=200)
    isAdmin = BooleanField(required=True)


class Club(Document):
    club_id = IntField(required=True, unique=True)
    title = StringField(required=True, max_length=200)
    url = StringField()
    leader_id = ReferenceField(User)


class Request(Document):
    posted = DateTimeField(required=True)
    date = DateField(required=True)
    u_id = ReferenceField(User, required=True)
    club_id = ReferenceField(Club)