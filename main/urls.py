from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name="index"),
    path('projects/', projects, name="projects"),
    path('contact/', contact, name="contact"),
    # path("", AjaxHandlerView.as_view(), name="index"),
]
