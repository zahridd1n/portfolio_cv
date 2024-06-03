from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cv/downloads', views.download_cv, name='download_cv'),
    path('about_me/', views.aboutme, name='about_me'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('portfolio/', views.portfolio, name='portfolio'),
]
