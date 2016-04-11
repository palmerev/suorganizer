# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(help_text='A label for URL config', max_length=63, unique_for_month='pub_date')),
                ('text', models.TextField()),
                ('pub_date', models.DateField(verbose_name='date published', auto_now_add=True)),
                ('startup', models.ManyToManyField(to='organizer.Startup', related_name='blog_posts')),
                ('tags', models.ManyToManyField(to='organizer.Tag', related_name='blog_posts')),
            ],
            options={
                'verbose_name': 'blog post',
                'get_latest_by': 'pub_date',
                'ordering': ['-pub_date', 'title'],
            },
        ),
    ]
