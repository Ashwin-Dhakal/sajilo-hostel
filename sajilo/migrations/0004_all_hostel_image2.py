# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-08 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sajilo', '0003_all_hostel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_hostel',
            name='image2',
            field=models.FileField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
