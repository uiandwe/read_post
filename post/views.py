from post.serializers import PostSerializer, TagSerializer
from post.models import Post, Tag
from django.shortcuts import render
from rest_framework.decorators import api_view
from .utils import api as util_api


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def post_list(request, pk=None):
    return util_api(request, pk, PostSerializer, Post)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def tag_list(request, pk=None):
    return util_api(request, pk, TagSerializer, Tag)


def index_view(request):
    return render(request, 'dist/index.html')
