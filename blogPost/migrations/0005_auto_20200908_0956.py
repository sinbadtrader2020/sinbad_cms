# Generated by Django 3.1.1 on 2020-09-08 09:56

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0004_blog_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=ckeditor.fields.RichTextField(max_length=300),
        ),
    ]
