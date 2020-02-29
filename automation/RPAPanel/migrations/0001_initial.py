# Generated by Django 2.2.7 on 2019-12-21 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('db_username', models.CharField(max_length=100)),
                ('db_password', models.CharField(default='', max_length=100)),
                ('db_host', models.CharField(default='', max_length=100)),
                ('db_port', models.IntegerField()),
                ('db_name', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'apps',
            },
        ),
        migrations.CreateModel(
            name='BotApsTracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appformno', models.CharField(blank=True, max_length=255, null=True)),
                ('app_no', models.CharField(blank=True, max_length=255, null=True)),
                ('upload_user', models.IntegerField()),
                ('ip_address', models.CharField(blank=True, max_length=45, null=True)),
                ('date', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'datacaptureapp',
            },
        ),
        migrations.CreateModel(
            name='BotApsTrackingBranch',
            fields=[
                ('tracking_id', models.AutoField(primary_key=True, serialize=False)),
                ('batchid', models.IntegerField(db_column='batchId')),
                ('appformno', models.CharField(db_column='AppFormNo', max_length=255)),
                ('apsno', models.CharField(db_column='apsNo', max_length=255)),
                ('branch', models.IntegerField(blank=True, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=255, null=True)),
                ('apptype', models.CharField(blank=True, db_column='appType', max_length=255, null=True)),
                ('entrydate', models.DateTimeField()),
                ('startdate', models.CharField(blank=True, db_column='startDate', max_length=50, null=True)),
                ('enddate', models.CharField(blank=True, db_column='endDate', max_length=50, null=True)),
                ('status', models.CharField(max_length=2)),
                ('iscamgen', models.IntegerField(blank=True, db_column='IsCamGen', null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'bot_aps_tracking',
            },
        ),
        migrations.CreateModel(
            name='Getfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('user_id', models.CharField(max_length=100)),
                ('upload_time', models.DateTimeField(auto_now=True, null=True)),
                ('total_record', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'bot_uploaded_files',
            },
        ),
        migrations.CreateModel(
            name='Hubs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ip', models.CharField(max_length=100)),
                ('port', models.CharField(default='', max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('process_id', models.IntegerField()),
            ],
            options={
                'db_table': 'hubs',
            },
        ),
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ip', models.CharField(max_length=100)),
                ('port', models.CharField(default='', max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('process_id', models.IntegerField()),
            ],
            options={
                'db_table': 'nodes',
            },
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ip', models.CharField(max_length=100)),
                ('port', models.CharField(default='', max_length=100)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('process_id', models.IntegerField()),
            ],
            options={
                'db_table': 'process',
            },
        ),
    ]
