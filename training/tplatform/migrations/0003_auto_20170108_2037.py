# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tplatform', '0002_auto_20170108_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=10, choices=[(1, b'Strategy'), (2, b'Content'), (3, b'Misc')]),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(max_length=100, choices=[(1, b'Tag1'), (2, b'Tag2'), (3, b'Tag3')]),
        ),
    ]
