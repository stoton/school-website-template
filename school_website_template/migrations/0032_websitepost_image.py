# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-02-04 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_website_template', '0031_websitepost_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='websitepost',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
