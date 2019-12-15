# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="APIKey",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("key", models.CharField(max_length=52)),
                ("description", models.CharField(blank=True, max_length=255)),
            ],
        )
    ]
