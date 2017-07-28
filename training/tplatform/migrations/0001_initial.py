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
                ('description', models.CharField(default=b'', max_length=350)),
                ('date_added', models.DateTimeField()),
                ('content', models.TextField()),
                ('category', models.IntegerField(choices=[(1, b'Strategy'), (2, b'Content'), (3, b'Misc')])),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('picture_handle', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=3, choices=[(1, b'CA'), (2, b'DCA'), (3, b'Trainer')])),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
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
            name='authors',
            field=models.ManyToManyField(to='tplatform.Author', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='related_articles',
            field=models.ManyToManyField(to='tplatform.Article', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='tplatform.Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='types',
            field=models.ManyToManyField(to='tplatform.Type', blank=True),
        ),
    ]
