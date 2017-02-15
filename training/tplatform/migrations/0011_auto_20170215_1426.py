# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tplatform', '0010_auto_20170121_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('picture_handle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('picture_handle', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.CharField(default=b'', max_length=350),
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(to='tplatform.Author', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='types',
            field=models.ManyToManyField(to='tplatform.Type', blank=True),
        ),
    ]
