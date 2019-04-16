import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from post.models import Post, Tag
from post.serializers import PostSerializer, TagSerializer, PostObjSerializer
from .utils import api as util_api


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def post_list(request, pk=None):
    if request.method == "GET":
        context_dict = []

        if pk:
            post = Post.objects.get(pk=pk)
            if post:
                context_dict = PostObjSerializer(post).run()
        else:
            search = request.GET.get('search', None)
            limit = request.GET.get('limit', 10)
            offset = request.GET.get('offset', 1)

            if search:
                posts = Post.objects.filter(Q(title__icontains=search))
            else:
                posts = Post.objects.all()

            if posts:
                paginator = Paginator(posts, limit)

                try:
                    pages = paginator.page(offset)
                except PageNotAnInteger:
                    pages = paginator.page(1)
                except EmptyPage:
                    pages = paginator.page(paginator.num_pages)

                context_dict = [PostObjSerializer(post).run() for post in pages]

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
