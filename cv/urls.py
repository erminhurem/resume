from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("de/", views.index_de, name="index_de")
]