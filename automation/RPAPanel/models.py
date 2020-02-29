from django.db import models
from django.db.models import Q
from model_utils import Choices

ORDER_COLUMN_CHOICES3 = Choices(
    ('0', 'id'),
    ('1', 'name'),
    ('2', 'db_username'),
    ('3', 'db_host'),
    ('4', 'db_port'),
    ('5', 'db_name'),
)

ORDER_COLUMN_CHOICES4 = Choices(
    ('0', 'id'),
    ('1', 'file_name'),
    ('2', 'user_id'),
    ('3', 'upload_time'),
    ('4', 'total_record'),
)

ORDER_COLUMN_CHOICES = Choices(
    ('0', 'id'),
    ('1', 'name'),
    ('2', 'ip'),
    ('3', 'port'),
    ('4', 'updated_at'),
    ('5', 'created_at'),
    ('6', 'process_id'),
)

ORDER_COLUMN_CHOICES1 = Choices(
    ('0', 'id'),
    ('1', 'appformno'),
    ('2', 'app_no'),
    ('3', 'upload_user'),
    ('4', 'ip_address'),
    ('5', 'date'),
)


# Create your models here.
class Apps(models.Model):
    objects = None
    name = models.CharField(max_length=100)  # blank=False
    db_username = models.CharField(max_length=100)  # blank=False
    db_password = models.CharField(max_length=100, default="", null=False)
    db_host = models.CharField(max_length=100, default="", null=False)
    db_port = models.IntegerField()
    db_name = models.CharField(max_length=100, default="", null=False)

    class Meta:
        db_table = "apps"


def query_apps_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = ORDER_COLUMN_CHOICES3[order_column]
    if order == 'desc':
        order_column = '-' + order_column

    queryset = Apps.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(id=search_value) |
                                   Q(name__icontains=search_value) |
                                   Q(db_username__icontains=search_value) |
                                   Q(db_password__icontains=search_value) |
                                   Q(db_host__icontains=search_value) |
                                   Q(db_port__icontains=search_value) |
                                   Q(db_name__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class Nodes(models.Model):
    objects = None
    name = models.CharField(max_length=100)  # blank=False
    ip = models.CharField(max_length=100)  # blank=False
    port = models.CharField(max_length=100, default="", null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    process_id = models.IntegerField()

    class Meta:
        db_table = "nodes"


def query_nodes_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = ORDER_COLUMN_CHOICES[order_column]
    if order == 'desc':
        order_column = '-' + order_column

    queryset = Nodes.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(id=search_value) |
                                   Q(name__icontains=search_value) |
                                   Q(ip__icontains=search_value) |
                                   Q(port__icontains=search_value) |
                                   Q(updated_at__icontains=search_value) |
                                   Q(created_at__icontains=search_value) |
                                   Q(process_id__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class Hubs(models.Model):
    objects = None
    name = models.CharField(max_length=100)  # blank=False
    ip = models.CharField(max_length=100)  # blank=False
    port = models.CharField(max_length=100, default="", null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    process_id = models.IntegerField()

    class Meta:
        db_table = "hubs"


def query_hubs_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = ORDER_COLUMN_CHOICES[order_column]
    if order == 'desc':
        order_column = '-' + order_column

    queryset = Hubs.objects.all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(id=search_value) |
                                   Q(name__icontains=search_value) |
                                   Q(ip__icontains=search_value) |
                                   Q(port__icontains=search_value) |
                                   Q(updated_at__icontains=search_value) |
                                   Q(created_at__icontains=search_value) |
                                   Q(process_id__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


# Create your models here.
class Process(models.Model):
    name = models.CharField(max_length=100)  # blank=False
    ip = models.CharField(max_length=100)  # blank=False
    port = models.CharField(max_length=100, default="", null=False)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    process_id = models.IntegerField()

    class Meta:
        db_table = "process"


class BotApsTracking(models.Model):
    objects = None
    appformno = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    app_no = models.CharField(max_length=255, blank=True, null=True)
    upload_user = models.IntegerField()
    ip_address = models.CharField(max_length=45, blank=True, null=True)
    date = models.DateField(auto_now=True, null=True)

    class Meta:
        db_table = 'datacaptureapp'


def query_bots_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = ORDER_COLUMN_CHOICES1[order_column]
    if order == 'desc':
        order_column = '-' + order_column

    queryset = BotApsTracking.objects.using('datacapture_db').all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(id=search_value) |
                                   Q(appformno__icontains=search_value) |
                                   Q(app_no__icontains=search_value) |
                                   Q(upload_user__icontains=search_value) |
                                   Q(ip_address__icontains=search_value) |
                                   Q(date__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class HhflStatusMst(models.Model):
    status = models.CharField(max_length=50)

    class Meta:
        db_table = 'hhfl_status_mst'


class HhflCustomerDtl(models.Model):
    app = models.ForeignKey('BotUploadedFiles', models.DO_NOTHING)
    cust_detail_no = models.CharField(max_length=50)
    applicant_type = models.CharField(max_length=20)
    cust_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'hhfl_customer_dtl'


class HhflDocumentMst(models.Model):
    doc_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'hhfl_document_mst'


class HhflDocumentDtl(models.Model):
    doc = models.ForeignKey('HhflDocumentMst', models.DO_NOTHING)
    cust = models.ForeignKey('HhflCustomerDtl', models.DO_NOTHING)
    filepath = models.CharField(max_length=255)

    class Meta:
        db_table = 'hhfl_document_dtl'


class HhflBankStatements(models.Model):
    doc_dtl = models.ForeignKey('HhflDocumentDtl', models.DO_NOTHING)
    bank_id = models.IntegerField()
    bank_name = models.CharField(max_length=255)
    is_verified = models.IntegerField()

    class Meta:
        db_table = 'hhfl_bank_statements'


class BotApsTrackingBranch(models.Model):
    objects = None
    bank_stat = models.ForeignKey('HhflBankStatements', models.DO_NOTHING)
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=100)  # Field name made lowercase.
    cheque_no = models.IntegerField()
    credit = models.CharField(max_length=255)
    debit = models.CharField(max_length=255)
    balance = models.FloatField()
    value_date = models.DateField()

    class Meta:
        db_table = 'hhfl_bank_statements_dtl'


def query_tracking_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    # order_column = kwargs.get('order[0][column]', None)[0]
    # order = kwargs.get('order[0][dir]', None)[0]

    # order_column = ORDER_COLUMN_CHOICES2[order_column]
    # if order == 'desc':
    #     order_column = '-' + order_column

    queryset = BotApsTrackingBranch.objects.using('datacapture_db').all()
    total = queryset.count()

    count = queryset.count()
    # queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class BotUploadedFiles(models.Model):
    objects = None
    case_id = models.IntegerField()
    created_on = models.CharField(max_length=20)
    app_status = models.ForeignKey('HhflStatusMst', models.DO_NOTHING, db_column='app_status')

    class Meta:
        db_table = 'hhfl_app_tracker'


def query_getfileviews_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = ORDER_COLUMN_CHOICES4[order_column]
    if order == 'desc':
        order_column = '-' + order_column

    queryset = BotUploadedFiles.objects.using('datacapture_db').all()
    total = queryset.count()

    if search_value:
        queryset = queryset.filter(Q(id=search_value) |
                                   Q(file_name__icontains=search_value) |
                                   Q(user_id__icontains=search_value) |
                                   Q(upload_time__icontains=search_value) |
                                   Q(total_record__icontains=search_value))

    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class BotErrorLogs(models.Model):
    objects = None
    log_id = models.AutoField(primary_key=True)
    exception_class = models.CharField(max_length=255, blank=True, null=True)
    txtappformno = models.CharField(db_column='txtAppFormNo', max_length=100, blank=True,
                                    null=True)  # Field name made lowercase.
    exception_dtl = models.CharField(max_length=5000, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    userid = models.IntegerField(db_column='userId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'bot_error_logs'


def query_error_by_args(**kwargs):
    draw = int(kwargs.get('draw', None)[0])
    queryset = BotErrorLogs.objects.using('datacapture_db').all()
    total = queryset.count()

    count = queryset.count()
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }
