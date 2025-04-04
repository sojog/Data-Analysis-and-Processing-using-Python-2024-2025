
from django.urls import path
from .views import formatie_2007_view, formatie_1994_view
## URL mic
urlpatterns = [
    path('2007', formatie_2007_view),
    path('1994', formatie_1994_view),
]
