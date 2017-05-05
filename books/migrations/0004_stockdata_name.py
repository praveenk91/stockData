# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20170502_0304'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockdata',
            name='name',
            field=models.CharField(default=datetime.datetime(2017, 5, 2, 6, 36, 36, 142310, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
