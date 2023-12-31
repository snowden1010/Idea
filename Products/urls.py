from . import views
from django.urls import path

app_name = "products"

urlpatterns = [
    path("home", views.index, name="home-page"),
    path("new/", views.new)
]