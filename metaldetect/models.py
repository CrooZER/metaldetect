from django.db import models
from location_field.models.plain import PlainLocationField

class PointGroup(models.Model):
    name = models.CharField(max_length=250, default='')
    color = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+ " : "+ self.name

class Point(models.Model):
    location = PlainLocationField(based_fields=['city'], zoom=7, null=True)
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, blank=True, null=True)
    group = models.ForeignKey(PointGroup, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+ " : "+ self.name    
    
