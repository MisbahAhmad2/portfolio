from django.shortcuts import render
from .models import Bio
from education.models import Education
from skills.models import Skill
from experience.models import Experience
from projects.models import Project

def home(request):
    return render(request, 'home.html')

def portfolio1(request):
    context = {
        'bio': Bio.objects.filter(person='person1').first(),
        'educations': Education.objects.filter(person='person1'),
        'skills': Skill.objects.filter(person='person1'),
        'experiences': Experience.objects.filter(person='person1'),
        'projects': Project.objects.filter(person='person1'),
    }
    return render(request, 'portfolio1.html', context)

def portfolio2(request):
    context = {
        'bio': Bio.objects.filter(person='person2').first(),
        'educations': Education.objects.filter(person='person2'),
        'skills': Skill.objects.filter(person='person2'),
        'experiences': Experience.objects.filter(person='person2'),
        'projects': Project.objects.filter(person='person2'),
    }
    return render(request, 'portfolio2.html', context)