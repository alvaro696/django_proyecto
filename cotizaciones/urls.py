from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('cotizar', views.cotizar),
]
