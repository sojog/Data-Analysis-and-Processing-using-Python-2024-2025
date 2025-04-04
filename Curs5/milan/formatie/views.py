from django.shortcuts import render

# Create your views here.

import pycountry

def formatie_2007_view(request):
    # https://dontpad.com/2007




    formatie = [ ('Dida', 'BR'), 
                ('Oddo', 'IT'),
                ('Nesta', 'IT'),  
                ('Maldini', 'IT'),
                ('Jankulovski', 'CZ') ,
                ('Gattuso', 'IT'),
                ('Pirlo', 'IT'), 
                ('Ambrosini', 'IT') , 
                ('Kaka', 'BR'),
                ('Seedors', 'NL'),
                ('Inzaghi', 'IT')]

    formatie = [ ('Dida', 'BR'), 
                ('Oddo', 'IT'),
                ('Nesta', 'IT'),  
                ('Maldini', 'IT'),
                ('Jankulovski', 'CZ') ,
                ('Gattuso', 'IT'),
                ('Pirlo', 'IT'), 
                ('Ambrosini', 'IT') , 
                ('Kaka', 'BR'),
                ('Seedors', 'NL'),
                ('Inzaghi', 'IT')]


    formatie = [ (j, pycountry.countries.get(alpha_2=n).flag )  for j,n in formatie  ]

    pozitionare = [1, 4, 3, 2, 1]


    pozitionare_formatie = []
    counter = 0
    for i in pozitionare:
        pozitionare_formatie.append(formatie[counter: counter + i])
        counter += i

    context = {
        'linii' : pozitionare_formatie
    }
    return render(request, "2007.html", context)

def formatie_1994_view(request):
    # https://dontpad.com/2007
    return render(request, "fotbal.html")