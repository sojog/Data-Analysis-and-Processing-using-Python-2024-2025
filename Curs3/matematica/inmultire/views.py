from django.shortcuts import render

# Create your views here.


def inmultire_view(request, num):

    valori = []
    num = int(num)
    for i in range(num+1):
        valori.append(f"{i} * {num} = {i * num}")

    context = {
        "num":num,
        "valori":valori
    }
    return render(request, "inmultire.html", context)