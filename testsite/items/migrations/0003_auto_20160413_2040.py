# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20160413_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='photoitem',
            name='deleted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tweetitem',
            name='deleted',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
