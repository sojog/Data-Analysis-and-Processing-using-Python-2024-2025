from django.shortcuts import render

# Create your views here.


def rock_paper_view (request):
    context = {}
    return render(request, "rock_paper.html", context)