import datetime
from django.contrib import admin
from ckeditor.fields import RichTextField,RichTextFormField,CKEditorWidget
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField,RichTextUploadingFormField
# Create your models here.

POST_CHOICES = (
    ('mostPopular','Most Popular'),
    ('recentPost', 'Recent Post')

)


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    blog_tittle = models.CharField(max_length=40)
    author_name = models.CharField(max_length=40)
    blog_cover = models.ImageField()
    blog_description = models.CharField(max_length=300)
    blog_content = RichTextUploadingField()
    blog_date = datetime.datetime.now()
    post = models.CharField(max_length=11, choices=POST_CHOICES, default='mostPopular')



