# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_website_template', '0013_auto_20170126_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='image',
            field=models.ImageField(default='gallery/znp.jpg', upload_to='gallery/'),
        ),
    ]
