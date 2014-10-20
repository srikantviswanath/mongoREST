from django.shortcuts import render
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from models.user_tmbnail import UserTmbNail
from serializers import UserTmbNailSerializer

class UserTmbNailList(ListCreateAPIView):
	queryset = UserTmbNail.objects.all()
	serializer_class = UserTmbNailSerializer

class UserTmbNailDetail(RetrieveUpdateDestroyAPIView):
	queryset = UserTmbNail.objects.all()
	serializer_class = UserTmbNailSerializer

