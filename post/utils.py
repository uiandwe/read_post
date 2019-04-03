# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.response import Response


def api(request, pk=None, obj_serializer=None, model=None, serializer_context=None):
    try:
        obj = None
        if pk:
            obj = model.objects.get(pk=pk)
        else:
            obj_list = model.objects.all()
    except model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if obj:
            serializer = obj_serializer(obj)
        else:
            if serializer_context:
                serializer = obj_serializer(instance=obj_list, context=serializer_context)
            else:
                serializer = obj_serializer(obj_list, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = obj_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        serializer = obj_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
