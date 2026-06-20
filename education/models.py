from django.db import models
from bio.models import PERSON_CHOICES

class Education(models.Model):
    person = models.CharField(max_length=10, choices=PERSON_CHOICES)
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    description = models.TextField(blank=True)
    gpa = models.CharField(max_length=20, blank=True) 


    def __str__(self):
        return f"{self.person} - {self.degree}"