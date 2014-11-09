from django.shortcuts import render
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from integ.models.common import PhotoFull
from integ.serializers.photo_full_serializer import PhotoFullSerializer
import django_filters
from rest_framework import generics


class PhotoFullList(ListCreateAPIView):
	model = PhotoFull
	serializer_class = PhotoFullSerializer
	
	def query_set(self):
		queryset = PhotoFull.objects.all()
		owner = self.request.QUERY_PARAMS.get('owner', None)
		title = self.request.QUERY_PARAMS.get('title', None)

		if owner is not None:
			queryset = queryset.filter(owner=owner)
		elif title is not None:
			queryset = queryset.filter(title=title)
		return queryset

class PhotoFullDetail(RetrieveUpdateDestroyAPIView):
	queryset = PhotoFull.objects.all()
	serializer_class = PhotoFullSerializer
