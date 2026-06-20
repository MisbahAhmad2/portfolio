from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio1/', views.portfolio1, name='portfolio1'),
    path('portfolio2/', views.portfolio2, name='portfolio2'),
]