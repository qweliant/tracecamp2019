# Generated by Django 2.0 on 2019-07-31 14:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20190731_0621'),
    ]

    operations = [
        migrations.AddField(
            model_name='movieapi',
            name='image',
            field=models.TextField(default='', validators=[django.core.validators.URLValidator()]),
        ),
    ]
