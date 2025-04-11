from django.shortcuts import render

# Create your views here.


def rock_paper_view (request):
    if request.method == "POST":
        print("Metoda -- POST")
        print(request.POST)
        client = request.POST.get("chosen")

        # Logica de business ...
        server = '...'
        rezultat = '...'

        context = {
            'client': 'Varianta clientului',
            'server': 'Varianta serverului',
            'rezultat' : 'Cineva a castigat'
        }
    else:
        print("Metoda -- GET")
        context = {}



    return render(request, "rock_paper.html", context)