# Generated by Django 3.0.3 on 2020-02-08 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0003_remove_county_varname_1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='county',
            name='nl_name_1',
        ),
    ]
