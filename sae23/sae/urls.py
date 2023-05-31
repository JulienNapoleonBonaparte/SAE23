from django.urls import path
from . import views

urlpatterns = [
    path('ajoutcategorie/', views.ajout),
    ]