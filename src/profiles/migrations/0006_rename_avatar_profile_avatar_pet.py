# Generated by Django 3.2.8 on 2021-10-21 10:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profile_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='avatar',
            new_name='avatar_pet',
        ),
    ]
