"""
"""
import rest_framework_filters as filters
from django.conf import settings

from . import models


class DataSetFilter(filters.FilterSet):
    """docstring for VenueServiceFilter"""
    class Meta:
        model = models.DataSet
        fields = {
            'title': settings.CHAR_LOOKUP,
            'description': settings.CHAR_LOOKUP,
            'image': settings.CHAR_LOOKUP
        }
