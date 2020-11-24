# Generated by Django 3.1.3 on 2020-11-24 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analysis', '0006_androidapp_thirdpartylibrarylist'),
    ]

    operations = [
        migrations.AddField(
            model_name='androidapp',
            name='meta_info_android_version',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='androidapp',
            name='meta_info_current_version',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='androidapp',
            name='meta_info_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='androidapp',
            name='meta_info_developer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='androidapp',
            name='meta_info_developer_email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='androidapp',
            name='meta_info_installs',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='androidapp',
            name='meta_info_last_update',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='androidapp',
            name='meta_info_rating',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='androidapp',
            name='meta_info_size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]