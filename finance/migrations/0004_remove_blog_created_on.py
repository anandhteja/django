# Generated by Django 3.2.9 on 2021-12-08 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_blog_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='Created_on',
        ),
    ]
