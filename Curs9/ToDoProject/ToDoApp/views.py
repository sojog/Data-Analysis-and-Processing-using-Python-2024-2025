from django.shortcuts import render, redirect
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

def create_todo_view(request):
	if request.method == "POST":
		print("Ai primit:", request.POST)

		new_task =  request.POST.get("task")
		if new_task:
			ToDoItem.objects.create(name=new_task)
			return redirect("todo_list_url")

	context = {}
	return render(request, 'create_todo.html', context)

def delete_todo_view(request, pk):
	todo_to_delete = ToDoItem.objects.get(id=pk)
	print("Todo urmator trebuie sters", todo_to_delete)

	todo_to_delete.delete()
	return  redirect("todo_list_url")


def update_todo_view(request, pk):
	if request.method == "POST":
		print("Ai primit:", request.POST)

		new_task =  request.POST.get("task")
		if new_task:
			task_to_update = ToDoItem.objects.get(id=pk)
			task_to_update.name = new_task
			task_to_update.save()

			return redirect("todo_list_url")


	todo_to_update = ToDoItem.objects.get(id=pk)
	print("Todo urmator trebuie sters", todo_to_update)

	context = {
		'todo_model':todo_to_update
	}


	return render(request, 'update_todo.html', context)

def mark_done_todo_view(request, pk):
	todo_to_mark = ToDoItem.objects.get(id=pk)
	print("Todo urmator trebuie sters", todo_to_mark)

	todo_to_mark.is_done = not todo_to_mark.is_done
	todo_to_mark.save()

	return  redirect("todo_list_url")