# Generated by Django 3.2.9 on 2021-12-19 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0011_blog_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='photo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
