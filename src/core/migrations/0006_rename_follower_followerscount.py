# Generated by Django 3.2.19 on 2023-07-16 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_follower'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follower',
            new_name='FollowersCount',
        ),
    ]
