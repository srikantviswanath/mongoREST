from integ.models.common import UserFull 
from rest_framework import serializers
from rest_framework_mongoengine.serializers import MongoEngineModelSerializer
from mongoengine import *
from photo_full_serializer import PhotoFullSerializer


class UserFullSerializer(MongoEngineModelSerializer):
	#photos = serializers.SlugRelatedField(many=True, read_only=True, slug_field="title")
	#photos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	#photos = PhotoFullSerializer()
	
	class Meta:
		model = UserFull
		exclude=("photos",)

