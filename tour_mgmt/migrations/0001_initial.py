# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('place', models.CharField(max_length=120, null=True, blank=True)),
                ('desc', models.TextField()),
                ('order', models.PositiveSmallIntegerField()),
                ('begin_date', models.DateField()),
                ('duration', models.PositiveSmallIntegerField(default=1)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'name', unique_with=[b'name'], editable=False)),
                ('desc', models.TextField()),
            ],
        ),
    ]
