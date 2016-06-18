# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='tour',
            field=models.ForeignKey(default=1, to='tour_mgmt.Tour'),
            preserve_default=False,
        ),
    ]
