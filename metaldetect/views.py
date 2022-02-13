from email.policy import HTTP
from http.client import HTTPResponse
from rest_framework import viewsets
from rest_framework import permissions
from django.shortcuts import render

from metaldetect.models import *
from metaldetect.serializers import *


def index(request):
    return render(request, 'index.html')


class ArtifactViewSet(viewsets.ModelViewSet):
    queryset = Artifact.objects.all().order_by('-created_at')
    serializer_class = ArtifactSerializer

class ArtifactTypeViewSet(viewsets.ModelViewSet):
    queryset = ArtifactType.objects.all().order_by('name')
    serializer_class = ArtifactTypeSerializer

class ArtifactPhotoViewSet(viewsets.ModelViewSet):
    queryset = ArtifactPhoto.objects.all()
    serializer_class = ArtifactPhotoSerializer

class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all().order_by('-created_at')
    serializer_class = PointSerializer

class PointGroupViewSet(viewsets.ModelViewSet):
    queryset = PointGroup.objects.all().order_by('-created_at')
    serializer_class = PointGroupSerializer

class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all().order_by('name')
    serializer_class = PeriodSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-created_at')
    serializer_class = EventSerializer