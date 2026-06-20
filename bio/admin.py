from django.contrib import admin
from .models import Bio

@admin.register(Bio)
class BioAdmin(admin.ModelAdmin):
    list_display = ('person', 'name', 'job_title')
    list_filter = ('person',)
    ordering = ('person',)