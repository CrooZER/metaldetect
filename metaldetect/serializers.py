from .models import *
from rest_framework import serializers

class ArtifactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Artifact
        fields = '__all__'

class ArtifactTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArtifactType
        fields = ['name']

class ArtifactPhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ArtifactPhoto
        fields = '__all__'  

class PointSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'

class PointGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PointGroup
        fields = '__all__'

class PeriodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Period
        fields = '__all__'

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'        