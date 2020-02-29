from django.db import models


class upload_file(models.Model):
    batch_id = models.IntegerField(null=False)
    app_no = models.CharField(max_length=50, null=False)
    aps_no = models.CharField(max_length=50, null=False)

    # def __str__(self):
    #     return self.name

    class Meta:
        db_table = "upload_file_data"
