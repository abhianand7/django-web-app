# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-14 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
        ('norecepieweb', '0003_auto_20161013_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Greet',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='norecepieweb_greet', serialize=False, to='cms.CMSPlugin')),
                ('guest_name', models.CharField(default='Guest', max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]