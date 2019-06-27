# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-26 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0011_auto_20190623_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='issue_type',
            field=models.CharField(choices=[('Bug', 'Bug'), ('Feature', 'Feature')], default='Feature', max_length=50),
        ),
        migrations.AlterField(
            model_name='bug',
            name='ticket_status',
            field=models.CharField(choices=[('Todo', 'Todo'), ('Doing', 'Doing'), ('Done', 'Done')], default='Todo', max_length=50),
        ),
    ]