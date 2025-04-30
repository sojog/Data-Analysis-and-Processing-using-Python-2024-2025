from django.shortcuts import render

# Create your views here.

def blog_list_view(request):
	context = {}
	return render(request, 'blog_list.html', context)

def blog_details_view(request):
	context = {}
	return render(request, 'blog_details.html', context)
