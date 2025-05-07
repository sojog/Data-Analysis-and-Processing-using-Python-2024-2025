from django.shortcuts import render
from .models import ToDoItem
# Create your views here.

def todo_list_view(request):
	todo_model_list = ToDoItem.objects.all()
	context = {
		'model_list' :  todo_model_list 
	}
	return render(request, 'todo_list.html', context)

def todo_details_view(request):
	context = {}
	return render(request, 'todo_details.html', context)
