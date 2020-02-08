from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
from .models import Incidence,County
class IncidenceAdmin(LeafletGeoAdmin):
    list_display = ('title','date_reported','location')
    search_fields = ('title',)
    filter_fields = ('title','date_reported')
admin.site.register(Incidence, IncidenceAdmin)


class CountyAdmin(LeafletGeoAdmin):
    list_display = ('name_1','cc_1')
    search_fields = ('name_1',)
    filter_fields = ('name_1','cc_1')
admin.site.register(County, CountyAdmin)