# Generated by Django 3.1.1 on 2020-09-07 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_content',
            field=models.CharField(max_length=300),
        ),
    ]
