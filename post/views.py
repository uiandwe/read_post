from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from post.serializers import PostSerializer, TagSerializer
from post.models import Post, Tag
from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def tag_list(request, pk=None):
    try:
        tag_obj = None
        if pk:
            tag_obj = Tag.objects.get(pk=pk)
        else:
            tag_obj_list = Tag.objects.all()
    except Tag.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if tag_obj:
            serializer = TagSerializer(tag_obj)
        else:
            serializer = TagSerializer(tag_obj_list, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = TagSerializer(tag_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tag_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




def index_view(request):
    return render(request, 'dist/index.html')
