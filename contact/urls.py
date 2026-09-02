from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.contact, name = "contact"),
    path("success/", views.contact_success,name =  "contact_success" )
]