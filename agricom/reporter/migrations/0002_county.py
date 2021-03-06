# Generated by Django 3.0.3 on 2020-02-08 08:36

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gid_0', models.CharField(max_length=80)),
                ('name_0', models.CharField(max_length=80)),
                ('gid_1', models.CharField(max_length=80)),
                ('name_1', models.CharField(max_length=80)),
                ('varname_1', models.CharField(max_length=80)),
                ('nl_name_1', models.CharField(max_length=80)),
                ('type_1', models.CharField(max_length=80)),
                ('engtype_1', models.CharField(max_length=80)),
                ('cc_1', models.CharField(max_length=80)),
                ('hasc_1', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
