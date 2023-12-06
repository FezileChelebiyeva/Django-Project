from django.urls import path
from students import views


urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("addpage/", views.addpage, name="add_page"),
    path("login/", views.login, name="login"),
]
