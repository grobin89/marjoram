# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ams.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('purchase_date', models.DateField()),
                ('warranty_period', models.PositiveSmallIntegerField()),
                ('value', models.DecimalField(max_digits=8, decimal_places=2)),
                ('depreciation_rate', models.DecimalField(max_digits=2, decimal_places=2)),
                ('registered', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='AssetExtendedFields',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('key', models.CharField(max_length=64)),
                ('value', models.CharField(max_length=64)),
                ('regex', models.CharField(max_length=128)),
                ('asset', models.ForeignKey(to='ams.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='AssetExtendedTemplate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('field_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='AssetLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('comment', models.TextField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('asset', models.ForeignKey(to='ams.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Incumbent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('full_name', models.CharField(default=ams.models.Incumbent.concat_name, max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('suburb', models.CharField(max_length=256)),
                ('post', models.CharField(max_length=4)),
                ('state', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=64)),
                ('assignment', models.CharField(default='IN', max_length=2, choices=[('IN', 'Incumbent'), ('SI', 'Site'), ('SE', 'Section'), ('ST', 'Stock')])),
                ('is_active', models.BooleanField(verbose_name=True)),
                ('incumbent', models.ForeignKey(to='ams.Incumbent')),
                ('location', models.ForeignKey(to='ams.Location')),
            ],
        ),
        migrations.CreateModel(
            name='RoleLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('comment', models.TextField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('role', models.ForeignKey(to='ams.Role')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('section_type', models.CharField(default='DE', max_length=2, choices=[('FA', 'Faculty'), ('DI', 'Division'), ('SC', 'School'), ('DE', 'Department')])),
            ],
        ),
        migrations.AddField(
            model_name='role',
            name='section',
            field=models.ForeignKey(to='ams.Section'),
        ),
        migrations.AddField(
            model_name='assetextendedtemplate',
            name='asset_type',
            field=models.ForeignKey(to='ams.AssetType'),
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_type',
            field=models.ForeignKey(to='ams.AssetType'),
        ),
        migrations.AddField(
            model_name='asset',
            name='role',
            field=models.ForeignKey(to='ams.Role'),
        ),
    ]
