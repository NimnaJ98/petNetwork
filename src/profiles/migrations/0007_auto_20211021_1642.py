# Generated by Django 3.2.8 on 2021-10-21 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_rename_avatar_profile_avatar_pet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar_pet',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar_pet.png', upload_to=''),
        ),
    ]
