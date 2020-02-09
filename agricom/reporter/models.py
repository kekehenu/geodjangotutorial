from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
# Create your models here.

from django.contrib.gis.db import models as gis_models
from django.db.models import Manager as GeoManager
# Create your models here.
class Incidence(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=250, null=True)
    date_reported = models.DateField(auto_now_add=True)
    location = gis_models.PointField(srid=4326)
    objects = GeoManager()
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural =" Incidences"

# This is an auto-generated Django model module created by ogrinspect.
class County(models.Model):
    gid_0 = models.CharField(max_length=80)
    name_0 = models.CharField(max_length=80)
    gid_1 = models.CharField(max_length=80)
    name_1 = models.CharField(max_length=80)
    #varname_1 = models.CharField(max_length=80)
    #nl_name_1 = models.CharField(max_length=80)
    type_1 = models.CharField(max_length=80)
    engtype_1 = models.CharField(max_length=80)
    cc_1 = models.CharField(max_length=80)
    hasc_1 = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)

#class Hopkin(models.Model):

