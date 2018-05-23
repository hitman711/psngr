from django.db import models

# Create your models here.


class DataSet(models.Model):
    """docstring for DataSet"""
    image = models.URLField(null=True, blank=True)
    description = models.TextField(blank=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.title
