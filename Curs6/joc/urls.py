from django.urls import path
from .views import *

urlpatterns = [
    path('clasic', rock_paper_view),
    path('frumos', rock_paper_scissors_lizzard_spock_view),

]
