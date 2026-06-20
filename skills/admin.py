from django.contrib import admin
from .models import Skill

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('person', 'name', 'skill_type', 'proficiency')
    list_filter = ('person', 'skill_type')
    ordering = ('person', 'skill_type')