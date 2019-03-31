from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from post.serializers import PostSerializer, TagSerializer
from post.models import Post, Tag
from django.http import Http404
from django.shortcuts import render


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


def index_view(request):
    return render(request, 'dist/index.html')
