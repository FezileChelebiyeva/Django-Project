from django.urls import path
from animals import views


urlpatterns = [
    path("animals/", views.index),
    path("animals/about/", views.about),
    path("animals/contact/", views.contact)
    ]
