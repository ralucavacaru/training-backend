# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tplatform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='status',
            field=models.IntegerField(default=3, choices=[(1, b'CA'), (2, b'DCA'), (3, b'Trainer'), (4, b'Contributor')]),
        ),
    ]
