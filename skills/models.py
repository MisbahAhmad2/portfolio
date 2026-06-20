from django.db import models
from bio.models import PERSON_CHOICES

class Skill(models.Model):
    SKILL_TYPES = [
        ('technical', 'Technical'),
        ('professional', 'Professional'),
    ]
    person = models.CharField(max_length=10, choices=PERSON_CHOICES)
    name = models.CharField(max_length=100)
    skill_type = models.CharField(max_length=20, choices=SKILL_TYPES)
    proficiency = models.IntegerField(default=80)

    def __str__(self):
        return f"{self.person} - {self.name}"