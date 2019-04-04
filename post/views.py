from post.serializers import PostSerializer, TagSerializer
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
        for post in posts:
            temp = {
                "pk": post.pk,
                "title": post.title,
                "post_url": post.post_url,
                "desc": post.desc,
                "thumbnail_link": post.thumbnail_link,
                "tags": []
            }

            tags = post.tags.all()
            if tags:
                temp["tags"] = [{"name":entry.name, "id":entry.id} for entry in tags]

            context_dict.append(temp)
        return HttpResponse(json.dumps({'data': context_dict}),
                            content_type='application/json; charset=utf8')
    else:
        return util_api(request, pk, PostSerializer, Post)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def tag_list(request, pk=None):
    return util_api(request, pk, TagSerializer, Tag)


def index_view(request):
    return render(request, 'dist/index.html')
