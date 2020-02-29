# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BotErrorLogs(models.Model):
    log_id = models.AutoField(primary_key=True)
    exception_class = models.CharField(max_length=255, blank=True, null=True)
    txtappformno = models.CharField(db_column='txtAppFormNo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    exception_dtl = models.CharField(max_length=5000, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'bot_error_logs'
