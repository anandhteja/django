# Generated by Django 3.2.9 on 2021-12-08 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0005_rename_blog_name_blog_created_by'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
