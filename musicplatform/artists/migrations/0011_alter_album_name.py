# Generated by Django 4.1.2 on 2022-10-15 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0010_alter_album_release'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(default='New Album', max_length=200, verbose_name='New Album'),
        ),
    ]
