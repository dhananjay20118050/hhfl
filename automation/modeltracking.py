# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BotApsTrackingBranch(models.Model):
    tracking_id = models.AutoField(primary_key=True)
    batchid = models.IntegerField(db_column='batchId')  # Field name made lowercase.
    appformno = models.CharField(db_column='AppFormNo', max_length=255)  # Field name made lowercase.
    apsno = models.CharField(db_column='apsNo', max_length=255)  # Field name made lowercase.
    branch = models.IntegerField(blank=True, null=True)
    branch_name = models.CharField(max_length=255, blank=True, null=True)
    apptype = models.CharField(db_column='appType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    entrydate = models.DateTimeField()
    startdate = models.CharField(db_column='startDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    enddate = models.CharField(db_column='endDate', max_length=50, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=2)
    iscamgen = models.IntegerField(db_column='IsCamGen', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'bot_aps_tracking'
