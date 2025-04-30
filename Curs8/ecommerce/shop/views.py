from django.shortcuts import render

# Create your views here.

def product_list_view(request):
	context = {}
	return render(request, 'product_list.html', context)

def product_details_view(request):
	context = {}
	return render(request, 'product_details.html', context)
