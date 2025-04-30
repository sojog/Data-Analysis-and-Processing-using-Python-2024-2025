from django.urls import path
from .views import *

urlpatterns = [
    path("all", blog_list_view),
    path("details/<int:blogid>", blog_details_view),
    path("details/<slug>", blog_details_view_with_slug)
]
