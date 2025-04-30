from django.shortcuts import render

# Create your views here.
from .models import BlogPost


def blog_list_view(request):
	blog_model_list = BlogPost.objects.all()

	context = {
		"blog_model_list" : blog_model_list
	}
	return render(request, 'blog_list.html', context)

def blog_details_view(request, blogid):
	current_blog_model = BlogPost.objects.filter(id=   blogid    )[0]
	context = {
		"current_blog_model" : current_blog_model
	}
	return render(request, 'blog_details.html', context)


def blog_details_view_with_slug(request, slug):
	current_blog_model = BlogPost.objects.filter(slug = slug)[0]
	context = {
		"current_blog_model" : current_blog_model
	}
	return render(request, 'blog_details.html', context)

