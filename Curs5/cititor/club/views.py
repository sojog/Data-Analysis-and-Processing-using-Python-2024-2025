from django.shortcuts import render
from datetime import datetime
# Create your views here.

def validare_cnp_view(request):
    context = {

    }
    return render(request, "formular_cnp.html", context)

def valideaza_cnp(cnp:str):
    if not cnp.isnumeric():
        return False
    if len(cnp) != 13:
        return False
    
    gen = int(cnp[0])
    if gen not in range(1, 9):
        return False
    
    an = int(cnp[1:3])
    today = datetime.now()

    if gen in (5, 6) and (2000 + an) > today.year:
        return False
    
    luna = int(cnp[3:5])
    if luna not in range(1, 13):
        return False
    
    zi = int(cnp[5:7])
    if zi not in range(1, 32):
        return False

    return True


def rezultat_cnp_view(request):
    print(request.POST)
    cnp = request.POST.get('cnp')
    print("CNP-ul primit este:", cnp)

    context = {
        'valid': valideaza_cnp(cnp)
    }
    return render(request, "rezultat_cnp.html", context)
