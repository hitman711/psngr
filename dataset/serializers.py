"""
"""
import logging
from rest_framework import serializers

from . import models

logs = logging.getLogger(__name__)


class DataSetSerializer(serializers.ModelSerializer):
    """docstring for DataSetSerializer"""
    class Meta:
        model = models.DataSet
        fields = '__all__'
