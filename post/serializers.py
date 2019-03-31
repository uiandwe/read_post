from post.models import Post, Type
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'