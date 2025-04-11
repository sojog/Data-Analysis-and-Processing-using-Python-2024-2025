from django.urls import path
from .views import *

urlpatterns = [
    path('', rock_paper_view),

]
