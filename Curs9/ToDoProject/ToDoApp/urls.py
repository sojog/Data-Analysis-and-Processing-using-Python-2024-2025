from django.urls import path
from .views import update_todo_view
from .views import delete_todo_view
from .views import create_todo_view
from .views import todo_details_view
from .views import todo_list_view

urlpatterns = [

	path("list", todo_list_view, name="todo_list_url"),
	path("details", todo_details_view),
	path("create", create_todo_view, name="create_todo_url"),
	path("delete/<int:pk>", delete_todo_view, name="delete_todo_url"),
	path("update/<int:pk>", update_todo_view, name="update_todo_url"),
]
