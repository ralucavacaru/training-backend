# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tplatform', '0003_auto_20170108_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.IntegerField(choices=[(1, b'Strategy'), (2, b'Content'), (3, b'Misc')]),
        ),
    ]
