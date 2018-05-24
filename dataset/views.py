"""
"""
from rest_framework import generics
from . import serializers, filters
# Create your views here.


class DataSetList(generics.ListAPIView):
    """API endpoint to List data from dataset model"""
    serializer_class = serializers.DataSetSerializer
    model_class = serializer_class.Meta.model
    queryset = model_class.objects.all()
    filter_class = filters.DataSetFilter
