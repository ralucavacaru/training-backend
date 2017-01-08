# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tplatform', '0005_auto_20170108_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.IntegerField(choices=[(1, b'Strategy'), (2, b'Content'), (3, b'Misc')]),
        ),
    ]
