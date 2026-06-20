from django.contrib import admin
from .models import Education

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('person', 'degree', 'institution', 'start_year', 'end_year')
    list_filter = ('person',)
    ordering = ('person', 'start_year')