# serializers.py
from rest_framework import serializers

from .models import Blog

class BLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ('id','blog_tittle','blog_description','author_name', 'blog_content','blog_date','blog_cover','post')


