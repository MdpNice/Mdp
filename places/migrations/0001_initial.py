# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-05 17:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('lng', models.DecimalField(decimal_places=9, max_digits=11)),
                ('lat', models.DecimalField(decimal_places=9, max_digits=11)),
                ('seen', models.BooleanField()),
                ('share', models.BooleanField(default=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('last_modif_date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
