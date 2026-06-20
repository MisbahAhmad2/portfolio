from django.db import models
from bio.models import PERSON_CHOICES

class Project(models.Model):
    person = models.CharField(max_length=10, choices=PERSON_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)

    def __str__(self):
        return f"{self.person} - {self.title}"