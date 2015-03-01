# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chill',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('longitude', models.DecimalField(decimal_places=14, max_digits=20)),
                ('latitude', models.DecimalField(decimal_places=14, max_digits=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('fbToken', models.CharField(max_length=100)),
                ('nick', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='chill',
            name='user',
            field=models.ForeignKey(to='JustChillBack.User'),
            preserve_default=True,
        ),
    ]
