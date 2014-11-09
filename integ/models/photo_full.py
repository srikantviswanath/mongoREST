from django.db import models
from mongoengine import *
import datetime
#from user_full import UserFull 

connect('displent-dev')
class PhotoFull(Document):
    path = StringField()
    title = StringField()
    #owner = ReferenceField(UserFull, reverse_delete_rule=CASCADE)
    location = StringField()
    date_taken = DateTimeField()
    tags = ListField(StringField())
    focal_length = IntField()
    
