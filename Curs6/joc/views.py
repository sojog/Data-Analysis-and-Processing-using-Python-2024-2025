from django.shortcuts import render

# Create your views here.


import random
import enum

class Optiuni(enum.Enum):
    Rock = 1
    Paper  = 2
    Scissors = 3
    Lizard = 4
    Spock = 5

    def __str__(self):
        return self.name

    @classmethod
    def values(cls):
        return [op.value for op in Optiuni]
    
    @classmethod
    def pairs(cls):
        return [(op.name, op.value) for op in Optiuni]

    def wins_over(self, other):
        WINNERS = {
            Optiuni.Rock : (Optiuni.Scissors, Optiuni.Lizard),
            Optiuni.Scissors : (Optiuni.Paper, Optiuni.Lizard),
            Optiuni.Paper : (Optiuni.Rock, Optiuni.Spock),
            Optiuni.Spock : (Optiuni.Scissors, Optiuni.Rock),
            Optiuni.Lizard : (Optiuni.Paper, Optiuni.Spock)
            
        }
        return other in WINNERS[self]


def logica_de_joc(client:int):
    client = Optiuni(client)
    server = Optiuni(random.choice(Optiuni.values()  ))

    if client == server:
        rezultat = "Egalitate"
    elif client.wins_over(server):
        rezultat = "Castig"
    else:
        rezultat = "Pierdere"

    return client, server, rezultat



def rock_paper_view (request):

    context = { 'pairs' : Optiuni.pairs()}

    if request.method == "POST":
        print("Metoda -- POST")
        print(request.POST)
        client = request.POST.get("chosen")

        # Logica de business ...
        if client and (client in map(str, Optiuni.values() )):
            alegere_client, alegere_server, rezultat_joc = logica_de_joc(int(client))
            context.update({
                'client': alegere_client,
                'server': alegere_server,
                'rezultat' : rezultat_joc,
            })


    else:
        print("Metoda -- GET")
        



    return render(request, "rock_paper.html", context)