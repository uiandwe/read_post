from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from post.serializers import PersonSerializer
from post.models import Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PersonSerializer
