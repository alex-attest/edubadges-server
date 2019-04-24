# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-22 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lti_edu', '0006_studentsenrolled_denied'),
    ]

    operations = [
        migrations.AddField(
            model_name='lticlient',
            name='entity_id',
            field=models.CharField(default=None, max_length=254, unique=False, null=True),
        ),
        migrations.AddField(
            model_name='lticlient',
            name='entity_version',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
