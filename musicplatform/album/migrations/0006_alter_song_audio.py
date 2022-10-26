# Generated by Django 4.1.2 on 2022-10-26 13:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0005_alter_song_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio',
            field=models.FileField(blank=True, upload_to='music', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])]),
        ),
    ]