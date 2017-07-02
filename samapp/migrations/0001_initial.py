# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='laundries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laundry_name', models.CharField(max_length=20)),
                ('city_area_mapid', models.IntegerField(max_length=10)),
                ('sector_id', models.IntegerField(max_length=10)),
                ('phone_no', models.IntegerField(default=10)),
            ],
        ),
    ]
