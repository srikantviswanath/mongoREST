from django.shortcuts import render
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from integ.models.user_full import UserFull
from integ.serializers.user_full_serializer import UserFullSerializer

class UserGistList(ListCreateAPIView):
	queryset = UserFull.objects.only("first_name", "last_name", "profile_pic", "membership")
	serializer_class = UserFullSerializer

class UserGistDetail(RetrieveUpdateDestroyAPIView):
	queryset = UserFull.objects.only("first_name", "last_name", "profile_pic", "membership")
	serializer_class = UserFullSerializer
