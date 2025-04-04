from django.shortcuts import render

# Create your views here.

def validare_cnp_view(request):
    context = {

    }
    return render(request, "formular_cnp.html", context)

