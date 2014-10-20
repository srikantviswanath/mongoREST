from integ.models.user_full import UserFull 
from rest_framework import serializers
from rest_framework_mongoengine.serializers import MongoEngineModelSerializer


class UserFullSerializer(MongoEngineModelSerializer):
	class Meta:
		model = UserFull
		exclude = ()

