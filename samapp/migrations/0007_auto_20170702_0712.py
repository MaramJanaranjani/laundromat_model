# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 07:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('samapp', '0006_areas_cities_city_are_map_dress_service_map_dresses_excess_cost_orders_sectors_services'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='city_are_map',
            new_name='city_areamap',
        ),
        migrations.RenameModel(
            old_name='dress_service_map',
            new_name='dress_servicemap',
        ),
    ]
