# Generated by Django 3.1.1 on 2020-09-08 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0007_auto_20200908_1121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='blog_content',
        ),
    ]