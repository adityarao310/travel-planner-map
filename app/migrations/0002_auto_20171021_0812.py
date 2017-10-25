# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=600)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=9, max_digits=12),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=9, max_digits=12),
        ),
    ]