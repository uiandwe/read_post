from post.serializers import PostSerializer, TagSerializer, PostObjSerializer
from post.models import Post, Tag
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from .utils import api as util_api
import json
from django.http import HttpResponse


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def post_list(request, pk=None):
    if request.method == "GET" and not pk:
        # TODO 페이지네이션 / 검색
        posts = Post.objects.all()
        context_dict = []

        if posts:
            context_dict = [PostObjSerializer(post).run() for post in posts]

        return HttpResponse(json.dumps({'data': context_dict}),
                            content_type='application/json; charset=utf8')
    else:
        return util_api(request, pk, PostSerializer, Post)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def tag_list(request, pk=None):
    if request.method == "GET" and pk:
        tag_obj = Tag.objects.get(pk=pk)
        posts = tag_obj.Tags.all()
        context_dict = []

        if posts:
            context_dict = [PostObjSerializer(post).run() for post in posts]

        return HttpResponse(json.dumps({'data': context_dict}),
                            content_type='application/json; charset=utf8')
    else:
        return util_api(request, pk, TagSerializer, Tag)


def index_view(request):
    return render(request, 'dist/index.html')
