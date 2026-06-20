from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('person', 'title', 'technologies')
    list_filter = ('person',)
    ordering = ('person',)