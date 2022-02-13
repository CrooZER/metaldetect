from datetime import date
from operator import mod
from os import name
from pyexpat import model
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
    group = models.ForeignKey(PointGroup, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+ " : "+ self.name  

class Period(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self) -> str:
        return self.name  

class Event(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class AtrifactType(models.Model):
    name = models.CharField(max_length=250)

    
class Artifact(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1000, blank=True)
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    period = models.ForeignKey(Period, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(AtrifactType, on_delete=models.SET_NULL, null=True)
    year = models.CharField(max_length=20, null=True)
    nominal = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





