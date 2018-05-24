"""
"""
from rest_framework import generics
from . import serializers, filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
# Create your views here.


class DataSetList(generics.ListAPIView):
    """API endpoint to List data from dataset model"""
    serializer_class = serializers.DataSetSerializer
    model_class = serializer_class.Meta.model
    queryset = model_class.objects.all()
    filter_class = filters.DataSetFilter

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(DataSetList, self).dispatch(*args, **kwargs)
