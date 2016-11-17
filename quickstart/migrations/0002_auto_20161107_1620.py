# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 16:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('producto', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='orden',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='orden',
            name='producto',
        ),
        migrations.AddField(
            model_name='line',
            name='orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quickstart.Orden'),
        ),
    ]
