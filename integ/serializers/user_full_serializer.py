from integ.models.common import UserFull, PhotoFull
from rest_framework import serializers
from rest_framework_mongoengine.serializers import MongoEngineModelSerializer
from mongoengine import *
from photo_full_serializer import PhotoFullSerializer
from integ.views. photo_full_view import PhotoFullList, PhotoFullDetail


class UserFullSerializer(MongoEngineModelSerializer):
	photos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	#photos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	#photos = PhotoFullSerializer()
	
	class Meta:
		model = UserFull
		exclude=() 


print "Hello"
