# Generated by Django 4.1.2 on 2022-10-14 21:56

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0008_remove_artist_assgin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='album',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='album',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
    ]
