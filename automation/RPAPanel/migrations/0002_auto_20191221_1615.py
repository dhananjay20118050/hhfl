# Generated by Django 2.2.7 on 2019-12-21 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RPAPanel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'bot_uploaded_files',
            },
        ),
        migrations.DeleteModel(
            name='Getfile',
        ),
    ]
