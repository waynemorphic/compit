from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('api/profiles/', views.ProfileList.as_view()),
    path('api/projects/', views.ProjectsList.as_view()),
]