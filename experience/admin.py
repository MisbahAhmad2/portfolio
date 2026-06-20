from django.contrib import admin
from .models import Experience

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('person', 'title', 'organization', 'exp_type', 'start_date', 'is_current')
    list_filter = ('person', 'exp_type', 'is_current')
    ordering = ('person', '-start_date')