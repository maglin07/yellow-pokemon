# Generated by Django 3.2.5 on 2021-07-17 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_author_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='following',
        ),
    ]