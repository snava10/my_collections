# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_collections', '0003_auto_20160726_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionitem',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]