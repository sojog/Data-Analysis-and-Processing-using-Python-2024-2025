"""
URL configuration for anibisecti project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import numpy as np
from django.http import HttpResponse

def ani_bisecti(request, start_year = 1899, stop_year = 2025):

    array = np.arange(start_year, stop_year + 1)
    years_array = array[(array % 400 == 0 ) |  ((array % 4 == 0) & (array % 100 != 0))]

    li_years = "\n".join(map(lambda x: f"<li>{x}</li>" ,years_array))

    return HttpResponse(f"<ol>{li_years} </ol>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ani_bisecti),
    path('<int:start_year>/<int:stop_year>', ani_bisecti),
]
