# Generated by Django 4.1.2 on 2022-10-09 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0004_alter_album_name_alter_artist_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_is_approved',
            field=models.BooleanField(default=True),
        ),
    ]
