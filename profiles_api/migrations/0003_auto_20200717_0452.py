# Generated by Django 2.2 on 2020-07-17 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0002_userprofilefeed'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfileFeed',
            new_name='ProfileFeedItem',
        ),
    ]
