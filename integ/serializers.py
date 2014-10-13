from .models import User, Comment, Post, ImagePost, TextPost, LinkPost
from rest_framework import serializers
from rest_framework_mongoengine.serializers import MongoEngineModelSerializer


class UserSerializer(MongoEngineModelSerializer):
	class Meta:
		model = User
		exclude = ('first_name', 'last_name')

class PostSerializer(MongoEngineModelSerializer):
	class Meta:
		model = TextPost
		exclude = ()