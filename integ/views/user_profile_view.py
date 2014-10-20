from django.shortcuts import render
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from integ.models.user_full import UserFull
from integ.serializers.user_full_serializer import UserFullSerializer

class UserProfileList(ListCreateAPIView):
	queryset = UserFull.objects.all()
	serializer_class = UserFullSerializer

class UserProfileDetail(RetrieveUpdateDestroyAPIView):
	queryset = UserFull.objects.all()
	serializer_class = UserFullSerializer

