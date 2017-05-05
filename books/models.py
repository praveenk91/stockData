# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Stockdata(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)  # AutoField?
    name = models.TextField(blank=True, null=True)
    exch = models.TextField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)
    price = models.TextField(blank=True, null=True)
    chng = models.TextField(blank=True, null=True)
    vol = models.TextField(blank=True, null=True)
    vol5 = models.TextField(blank=True, null=True)
    vol10 = models.TextField(blank=True, null=True)
    vol30 = models.TextField(blank=True, null=True)
    prevclose = models.TextField(db_column='prevClose', blank=True, null=True)  # Field name made lowercase.
    openprice = models.TextField(db_column='openPrice', blank=True, null=True)  # Field name made lowercase.
    bidprice = models.TextField(db_column='bidPrice', blank=True, null=True)  # Field name made lowercase.
    offrprice = models.TextField(db_column='offrPrice', blank=True, null=True)  # Field name made lowercase.
    vwap = models.TextField(blank=True, null=True)
    buyqty = models.TextField(db_column='buyQty', blank=True, null=True)  # Field name made lowercase.
    sellqty = models.TextField(db_column='sellQty', blank=True, null=True)  # Field name made lowercase.
    low = models.TextField(blank=True, null=True)
    high = models.TextField(blank=True, null=True)
    low52 = models.TextField(blank=True, null=True)
    high52 = models.TextField(blank=True, null=True)
    lowprc = models.TextField(db_column='lowPrc', blank=True, null=True)  # Field name made lowercase.
    highprc = models.TextField(db_column='highPrc', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'stockData'
