# Generated by Django 4.1.2 on 2022-10-07 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='Social_link',
            field=models.URLField(blank=True, max_length=100),
        ),
    ]
