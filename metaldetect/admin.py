from django.contrib import admin


from .models import *


class PointGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')

class PointAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')




admin.site.register(PointGroup, PointGroupAdmin)
admin.site.register(Point, PointAdmin)
admin.site.register(Period)
admin.site.register(Event)
admin.site.register(ArtifactType)
admin.site.register(Artifact)