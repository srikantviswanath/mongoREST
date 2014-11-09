from django.db import models
from mongoengine import *
import datetime
#from user_full import UserFull 

connect('displent-dev')
class PhotoFull(Document):
    path = StringField()
    title = StringField()
    owner = ReferenceField('UserFull')
    location = StringField()
    date_taken = DateTimeField()
    tags = ListField(StringField())
    focal_length = IntField()
    

class UserFull(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    profile_pic = StringField()
    member_since = DateTimeField()
    membership = StringField()
    theme_pic = StringField()
    photos = ListField(ReferenceField(PhotoFull, reverse_delete_rule=CASCADE))

