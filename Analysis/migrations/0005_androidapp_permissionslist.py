# Generated by Django 3.1.3 on 2020-11-24 00:56

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('Analysis', '0004_auto_20201124_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='androidapp',
            name='PermissionsList',
            field=django_mysql.models.ListCharField(models.CharField(max_length=99), blank=True, max_length=5000, null=True, size=50),
        ),
    ]
