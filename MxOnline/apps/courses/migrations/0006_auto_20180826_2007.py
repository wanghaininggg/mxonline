# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-26 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='tag',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='\u8bfe\u7a0b\u6807\u7b7e'),
        ),
    ]
