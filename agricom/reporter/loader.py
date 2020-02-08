import os
from django.contrib.gis.utils import LayerMapping
from .models import County

# Auto-generated `LayerMapping` dictionary for County model  begin----
county_mapping = {
    'gid_0': 'GID_0',
    'name_0': 'NAME_0',
    'gid_1': 'GID_1',
    'name_1': 'NAME_1',
    #'varname_1': 'VARNAME_1',
    #'nl_name_1': 'NL_NAME_1',
    'type_1': 'TYPE_1',
    'engtype_1': 'ENGTYPE_1',
    'cc_1': 'CC_1',
    'hasc_1': 'HASC_1',
    'geom': 'MULTIPOLYGON',
}
# Auto-generated `LayerMapping` dictionary for County model  end-------

county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'gadm36_KEN_1.shp'),)

def run(verbose=True):
    lm = LayerMapping(County, county_shp, county_mapping, transform= False,encoding='iso-8859-1')
    lm.save(strict=True,verbose=verbose)