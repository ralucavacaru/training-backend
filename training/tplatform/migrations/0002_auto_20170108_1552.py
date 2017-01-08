# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tplatform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(max_length=10, choices=[(b'STRATEGY', b'Strategy'), (b'CONTENT', b'Content'), (b'MISC', b'Misc')]),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(max_length=100, choices=[(b'TAG1', b'Tag1'), (b'TAG2', b'Tag2'), (b'TAG3', b'Tag3')]),
        ),
    ]
