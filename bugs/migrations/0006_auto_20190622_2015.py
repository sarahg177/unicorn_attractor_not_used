# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-22 20:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0005_bug_ticket_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bug',
            old_name='name',
            new_name='title',
        ),
    ]