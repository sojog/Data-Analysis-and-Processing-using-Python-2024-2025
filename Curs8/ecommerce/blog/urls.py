from django.urls import path
from .views import *

urlpatterns = [
    path("all", blog_list_view),
    path("details", blog_details_view)
]
