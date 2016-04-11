# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=63)),
                ('pub_date', models.DateField(verbose_name='date published')),
                ('link', models.URLField(max_length=255)),
            ],
            options={
                'verbose_name': 'news article',
                'ordering': ['-pub_date'],
                'get_latest_by': 'pub_date',
            },
        ),
        migrations.CreateModel(
            name='Startup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(db_index=True, max_length=31)),
                ('slug', models.SlugField(help_text='A label for URL config', max_length=31)),
                ('description', models.TextField()),
                ('founded_date', models.DateField(verbose_name='date founded')),
                ('contact', models.EmailField(max_length=254)),
                ('website', models.URLField(max_length=255)),
            ],
            options={
                'ordering': ['name'],
                'get_latest_by': 'founded_date',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=31, unique=True)),
                ('slug', models.SlugField(help_text='A label for URL config', max_length=31, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='startup',
            name='tags',
            field=models.ManyToManyField(to='organizer.Tag'),
        ),
        migrations.AddField(
            model_name='newslink',
            name='startup',
            field=models.ForeignKey(to='organizer.Startup'),
        ),
    ]
