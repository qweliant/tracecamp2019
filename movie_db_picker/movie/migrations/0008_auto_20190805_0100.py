# Generated by Django 2.2.4 on 2019-08-05 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20190805_0043'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MovieTest',
            new_name='Movie',
        ),
    ]
