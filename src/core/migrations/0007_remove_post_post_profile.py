# Generated by Django 3.2.19 on 2023-07-18 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_follower_followerscount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_profile',
        ),
    ]
