from django.shortcuts import render
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from integ.models.common import UserFull
from integ.serializers.user_full_serializer import UserFullSerializer
import json
from bson.objectid import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            print obj
            return str(obj)
        else:
        	#return obj
        	#raise TypeError("Unserializable object {} of type {}".format(obj,type(obj)))
        	json.JSONEncoder.default(self,obj)

class UserProfileList(ListCreateAPIView):
	queryset = UserFull.objects.all()
	queryset = JSONEncoder().encode(queryset)
	serializer_class = UserFullSerializer

class UserProfileDetail(RetrieveUpdateDestroyAPIView):
	queryset = UserFull.objects.all()
	serializer_class = UserFullSerializer

