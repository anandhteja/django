# Generated by Django 3.2.9 on 2021-12-19 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0009_alter_blog_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='photo',
        ),
    ]
