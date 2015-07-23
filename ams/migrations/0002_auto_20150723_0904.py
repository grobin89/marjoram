# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ams', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='active',
            new_name='is_active',
        ),
        migrations.AlterField(
            model_name='role',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
