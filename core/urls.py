from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name = 'home/'),
    path('home/', views.home, name = 'home/'),
    path('accounts/register/home/', views.home, name = 'home/'),
    path('accounts/login/', auth_views.LoginView.as_view(next_page = 'home/'), name = 'login'),
    path('accounts/login/home/', views.home, name = 'home/'),
    path('api/profiles/', views.ProfileList.as_view()),
    path('api/projects/', views.ProjectsList.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)