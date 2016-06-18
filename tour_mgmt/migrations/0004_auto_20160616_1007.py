# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('image_gallery', '0001_initial'),
        ('tour_mgmt', '0003_auto_20160519_0710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stage',
            options={'ordering': ['tour__name', 'order']},
        ),
        migrations.AddField(
            model_name='tour',
            name='gallery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='image_gallery.Gallery'),
        ),
    ]