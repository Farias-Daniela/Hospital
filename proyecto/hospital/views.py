from django.shortcuts import render


def oftalmologia(request):
    #return HttpResponse("Hola, tiene bien sus ojos?")
    return render(request, "hospital/oftalmologia.html")

def pediatria(request):
    xx = [
    {
        "nombre": "Dra. Mariana López",
        "telefono": "341-555-1234",
        "horario": "Lun a Vie - 08:00 a 14:00"
    },
    {
        "nombre": "Dr. Tomás García",
        "telefono": "341-555-5678",
        "horario": "Lun a Vie - 10:00 a 16:00"
    },
    {
        "nombre": "Dra. Lucía Ramírez",
        "telefono": "341-555-9012",
        "horario": "Martes y Jueves - 09:00 a 13:00"
    },
    {
        "nombre": "Dr. Federico Alvarez",
        "telefono": "341-555-3456",
        "horario": "Lunes, Miércoles y Viernes - 13:00 a 18:00"
    },
    {
        "nombre": "Dra. Camila Fernández",
        "telefono": "341-555-7890",
        "horario": "Lunes a Jueves - 08:30 a 12:30"
    }
    ]

    contexto = {
        "pediatras": xx,
        "cirujia": xx,
        "psiquiatria": xx,
    }
    return render(request, "hospital/pediatria.html", context=contexto)

def cirujia(request):
    return render(request, "hospital/cirujia.html", context=contexto)

def psiquiatria(request):
    return render(request, "hospital/psiquiatria.html", context=contexto)



# Create your views here.
