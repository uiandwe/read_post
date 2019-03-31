from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from post.serializers import PostSerializer, TypeSerializer
from post.models import Post, Type
from django.http import Http404
from django.shortcuts import render


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


def index_view(request):
    return render(request, 'dist/index.html')
