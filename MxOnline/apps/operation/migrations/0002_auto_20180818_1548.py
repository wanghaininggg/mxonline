# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-18 15:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_type',
            field=models.IntegerField(choices=[(1, '\u8bfe\u7a0b'), (2, '\u8bfe\u7a0b\u673a\u6784'), (3, '\u8bb2\u5e08')], default=1, verbose_name='\u6536\u85cf\u7c7b\u578b'),
        ),
    ]
