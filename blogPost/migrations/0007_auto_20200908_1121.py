# Generated by Django 3.1.1 on 2020-09-08 11:21

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0006_auto_20200908_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]