# Generated by Django 3.1.1 on 2020-09-08 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogPost', '0003_auto_20200907_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='post',
            field=models.CharField(choices=[('mostPopular', 'Most Popular'), ('recentPost', 'Recent Post')], default='mostPopular', max_length=11),
        ),
    ]