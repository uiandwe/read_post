from post.models import Post, Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('created', 'tags')

    # def get_validation_exclusions(self, *args, **kwargs):
    #     exclusions = super(PostSerializer, self).get_validation_exclusions()
    #
    #     return exclusions + ['test']

    def create(self, validated_data):
        print("validated_data", validated_data)
        str_tags = self.initial_data['tags']

        tag_list = str_tags.split(",")

        instance = Post.objects.create(**validated_data)

        tags = Tag.objects.filter(id__in=tag_list)
        for tag in tags:
            instance.tags.add(tag)

        return instance
