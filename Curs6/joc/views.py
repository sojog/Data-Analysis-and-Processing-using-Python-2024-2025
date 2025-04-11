from django.shortcuts import render

# Create your views here.


import random
import enum

class Optiuni(enum.Enum):
    Rock = 1
    Paper  = 2
    Scissors = 3

    def __str__(self):
        return self.name



def logica_de_joc(client:int):
    client = Optiuni(client)
    server = Optiuni(random.choice([1, 2, 3]))

    if client == server:
        rezultat = "Egalitate"
    elif client == Optiuni.Rock and server == Optiuni.Scissors:
        rezultat = "Castig"
    elif client == Optiuni.Scissors and server == Optiuni.Paper:
        rezultat = "Castig"
    elif client == Optiuni.Paper and server == Optiuni.Rock:
        rezultat = "Castig"
    else:
        rezultat = "Pierdere"

    return client, server, rezultat



def rock_paper_view (request):
    if request.method == "POST":
        print("Metoda -- POST")
        print(request.POST)
        client = request.POST.get("chosen")

        # Logica de business ...
        if client and (client in ("1", "2", "3")):
            alegere_client, alegere_server, rezultat_joc = logica_de_joc(int(client))
            context = {
                'client': alegere_client,
                'server': alegere_server,
                'rezultat' : rezultat_joc
            }
        else:
            context = { }
    else:
        print("Metoda -- GET")
        context = {}



    return render(request, "rock_paper.html", context)