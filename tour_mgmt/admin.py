from django.db import models
from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from djangocms_text_ckeditor.widgets import TextEditorWidget
from .models import Tour, Stage

def duplicate_stage(modeladmin, request, queryset):
    for object in queryset:
        object.id = None
        object.save()
duplicate_stage.short_description = "Copier une etape"

class StageAdmin(LeafletGeoAdmin):
    model = Stage
    fieldsets = (
        (None, {
            'fields': (('tour', 'order','begin_date', 'duration'),
                        ('name', 'place'),
                        'desc',
                        'point')
        }),
    )
    list_display = ('id', 'tour',  'name', 'order', 'begin_date', 'duration',)
    list_filter = ('tour__name',)
    list_editable = ('tour', 'order', 'begin_date', 'duration')
    formfield_overrides = {
        models.TextField: {'widget': TextEditorWidget },
    }
    actions = [duplicate_stage]

class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'ongoing')
    list_editable = ('ongoing', )
    formfield_overrides = {
        models.TextField: {'widget': TextEditorWidget }
    }
admin.site.register(Tour, TourAdmin)
admin.site.register(Stage, StageAdmin)
