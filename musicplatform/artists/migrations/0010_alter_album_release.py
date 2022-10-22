# Generated by Django 4.1.2 on 2022-10-15 00:21

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0009_remove_album_pub_date_album_created_album_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='release',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='release'),
        ),
    ]
