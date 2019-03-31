from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    url = models.CharField(max_length=200, null=False)
    desc = models.TextField(null=False)
    thumbnail_link = models.CharField(max_length=200, null=True)
    types = models.ManyToManyField(Type, blank=True, null=True, related_name="types")
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title