# Generated by Django 3.1.3 on 2020-11-24 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Analysis', '0009_androidapp_decompile_successful'),
    ]

    operations = [
        migrations.AddField(
            model_name='androidapp',
            name='xapk',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
