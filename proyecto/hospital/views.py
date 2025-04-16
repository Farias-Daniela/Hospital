from django.shortcuts import render


def oftalmologia(request):
    #return HttpResponse("Hola, tiene bien sus ojos?")
    return render(request, "hospital/oftalmologia.html")
# Create your views here.
