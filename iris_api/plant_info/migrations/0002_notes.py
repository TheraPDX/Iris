# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-21 00:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant_info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_content', models.CharField(max_length=500)),
                ('note_date', models.DateTimeField()),
            ],
        ),
    ]
