# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20170426_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='stockData',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('exch', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('chng', models.CharField(max_length=50)),
                ('vol', models.CharField(max_length=50)),
                ('vol5', models.CharField(max_length=50)),
                ('vol10', models.CharField(max_length=50)),
                ('vol30', models.CharField(max_length=50)),
                ('prevClose', models.CharField(max_length=50)),
                ('openPrice', models.CharField(max_length=50)),
                ('bidPrice', models.CharField(max_length=50)),
                ('offrPrice', models.CharField(max_length=50)),
                ('vwap', models.CharField(max_length=50)),
                ('buyQty', models.CharField(max_length=50)),
                ('sellQty', models.CharField(max_length=50)),
                ('low', models.CharField(max_length=50)),
                ('high', models.CharField(max_length=50)),
                ('low52', models.CharField(max_length=50)),
                ('high52', models.CharField(max_length=50)),
                ('lowPrc', models.CharField(max_length=50)),
                ('highPrc', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
