from django.db import models

from mongoengine import *
import datetime

connect('mongoREST')
class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

    def __str__(self):
    	return self.first_name 

class Comment(EmbeddedDocument):
	content = StringField()
	name = StringField(max_length=120)

class Post(Document):
	title = StringField(max_length=120, required=True)
	author = ReferenceField(User, reverse_delete_rule=CASCADE)
	tags = ListField(StringField(max_length=30))
	comments = ListField(EmbeddedDocumentField(Comment))

	def __str__(self):
		return self.title

	meta = {'allow_inheritance':True}

class TextPost(Post):
	content = StringField()

	def __str__(self):
		return self.title

class ImagePost(Post):
	image_path = StringField()

class LinkPost(Post):
	link_url = StringField()

class Recipient(Document):
	name = StringField()
	email = EmailField()