# Generated by Django 4.1.2 on 2022-10-08 22:17

import artists.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0003_alter_artist_stage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(default='New Album', max_length=200,  verbose_name='New Album'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='Stage',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
