from django.db import models

PERSON_CHOICES = [
    ('person1', 'Person 1'),
    ('person2', 'Person 2'),
]

class Bio(models.Model):
    person = models.CharField(max_length=10, choices=PERSON_CHOICES, unique=True)
    name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile/', blank=True)
    description = models.TextField()
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)


    def __str__(self):
        return f"{self.person} - {self.name}"