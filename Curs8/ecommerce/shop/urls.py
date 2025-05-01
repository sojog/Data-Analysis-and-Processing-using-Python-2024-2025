from django.urls import path
from .views import *


urlpatterns = [
    path("all", product_list_view),
    path("details/<slug>", product_details_view)
]
