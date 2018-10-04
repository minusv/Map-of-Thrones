"""
Atlas Models Configuration
"""

from django.db import models

class Kingdoms(models.Model):
    name = models.CharField(max_length=100)
    claimedby = models.CharField(max_length=100)
    summary = models.TextField()
    awoiaf_url = models.URLField()

    def __str__(self):
        return self.name

class Locations(models.Model):
    name = models.CharField(max_length=100)
    location_type = models.CharField(max_length=100)
    summary = models.TextField()
    awoiaf_url = models.URLField()
    kingdom = models.ForeignKey(Kingdoms, on_delete=models.CASCADE)

    def __str__(self):
        return self.name