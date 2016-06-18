# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_mgmt', '0002_stage_tour'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='ongoing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stage',
            name='tour',
            field=models.ForeignKey(related_name='stages', to='tour_mgmt.Tour'),
        ),
    ]
