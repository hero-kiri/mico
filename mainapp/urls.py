from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('doctor/', views.doctor, name='doctor'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('treatment/', views.treatment, name='treatment'),
]
