from django.shortcuts import render
from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from integ.models import User, Comment, Post, LinkPost, TextPost, ImagePost
from integ.serializers import UserSerializer, PostSerializer

class UserList(ListCreateAPIView):
	queryset = User.objects.only('email')
	serializer_class = UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class PostList(ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
