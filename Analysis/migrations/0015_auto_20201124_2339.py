# Generated by Django 3.1.3 on 2020-11-24 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analysis', '0014_androidapp_privacy_policy_access'),
    ]

    operations = [
        migrations.AddField(
            model_name='androidapp',
            name='ThirdPartyTrackingLibrary',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='androidapp',
            name='dangerous_permission',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]