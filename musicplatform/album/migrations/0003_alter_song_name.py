# Generated by Django 4.1.2 on 2022-10-24 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(blank=True, help_text="if no name is provided, the song's name defaults to the album name", max_length=200),
        ),
    ]