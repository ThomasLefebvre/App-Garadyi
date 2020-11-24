# Generated by Django 3.1.3 on 2020-11-24 00:57

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('Analysis', '0005_androidapp_permissionslist'),
    ]

    operations = [
        migrations.AddField(
            model_name='androidapp',
            name='ThirdPartyLibraryList',
            field=django_mysql.models.ListCharField(models.CharField(max_length=99), blank=True, max_length=5000, null=True, size=50),
        ),
    ]
