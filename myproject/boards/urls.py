from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bond', views.bond, name='bond')
]
