# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tplatform', '0004_auto_20170108_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.IntegerField(choices=[(b'STRATEGY', b'Strategy'), (b'CONTENT', b'Content'), (b'MISC', b'Misc')]),
        ),
    ]
