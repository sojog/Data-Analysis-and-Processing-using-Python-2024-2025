from django.urls import path
from .views import todo_details_view
from .views import todo_list_view

urlpatterns = [

	path("list", todo_list_view),
	path("details", todo_details_view),
]
