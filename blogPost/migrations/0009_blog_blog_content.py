# Generated by Django 3.1.1 on 2020-09-08 12:34

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0008_remove_blog_blog_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=0),
            preserve_default=False,
        ),
    ]
