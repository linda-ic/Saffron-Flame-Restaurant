from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),

    path('menu/', views.menu, name='menu'),

    path('contact/', views.contact, name='contact'),

    path('reservations/', views.reservations, name='reservation'),
]