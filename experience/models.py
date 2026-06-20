from django.db import models
from bio.models import PERSON_CHOICES

class Experience(models.Model):
    EXP_TYPES = [
        ('academic', 'Academic'),
        ('professional', 'Professional'),
    ]
    person = models.CharField(max_length=10, choices=PERSON_CHOICES)
    title = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    exp_type = models.CharField(max_length=20, choices=EXP_TYPES)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.person} - {self.title}"