from django.db import models
from mongoengine import *
import datetime
from photo_full import PhotoFull

connect('displent-dev')
class UserFull(Document):
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    profile_pic = StringField()
    member_since = DateTimeField()
    membership = StringField()
    theme_pic = StringField()
    photos = ListField(ReferenceField(PhotoFull, reverse_delete_rule=CASCADE))

