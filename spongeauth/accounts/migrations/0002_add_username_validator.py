# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-14 01:19
from __future__ import unicode_literals

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=20, unique=True, validators=[accounts.models.validate_username]),
        )
    ]
