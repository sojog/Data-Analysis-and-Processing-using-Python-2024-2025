
from django.urls import path

from .views import validare_cnp_view

## URL MIC
urlpatterns = [
  path('cnp', validare_cnp_view)
]
