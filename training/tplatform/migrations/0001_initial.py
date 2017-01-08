# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField()),
                ('content', models.TextField()),
                ('category', models.CharField(max_length=1, choices=[(b'STRATEGY', b'Strategy'), (b'CONTENT', b'Content'), (b'MISC', b'Misc')])),
                ('tags', models.CharField(max_length=3, choices=[(b'TAG1', b'Tag1'), (b'TAG2', b'Tag2'), (b'TAG3', b'Tag3')])),
            ],
        ),
    ]
