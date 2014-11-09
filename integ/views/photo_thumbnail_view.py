from django.shortcuts import render
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from integ.models.common import PhotoFull
from integ.serializers.photo_full_serializer import PhotoThumbnailSerializer

class PhotoThumbnailList(ListCreateAPIView):
	queryset = PhotoFull.objects.only("path", "title", "owner", "tags")
	serializer_class = PhotoThumbnailSerializer

class PhotoThumbnailDetail(RetrieveUpdateDestroyAPIView):
	queryset = PhotoFull.objects.only("path", "title", "owner", "tags")
	serializer_class = PhotoThumbnailSerializer
