from integ.models.common import PhotoFull
from rest_framework import serializers
from rest_framework_mongoengine.serializers import MongoEngineModelSerializer
import django_filters
from rest_framework import generics

class PhotoFullSerializer(MongoEngineModelSerializer):
	owner = serializers.CharField(source="owner.id", read_only=True)

	class Meta:
		model = PhotoFull
		exclude = ()

class PhotoThumbnailSerializer(MongoEngineModelSerializer):
	#owner = serializers.CharField(source="owner.id", read_only=True)
	class Meta:
		model = PhotoFull
		exclude = ()

