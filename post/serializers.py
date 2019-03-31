from post.models import Post, Tag
from rest_framework import serializers


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'url', 'desc', 'tags', 'created')

    def create(self, validated_data):
        print("validated_data", validated_data)
        order = Tag.objects.get(pk=validated_data.pop('tags'))
    #     # instance = Post.objects.create(**validated_data)
    #     # Assignment.objects.create(Order=order, Equipment=Equipment)
    #     return
