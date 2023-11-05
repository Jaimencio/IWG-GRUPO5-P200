from django.shortcuts import render
from django.http import HttpResponse
from .models import Datos
from django.http import JsonResponse




# Create your views here.

def get_plants(request):
    plants= Datos.objects.values('planta').distinct()
    listplants=[]
    for el in plants:
        y='planta'
        x=el['planta']
        listplants.append(x)
    context1= {'plants': plants}
    return render(request, 'menu/base.html', context1)
   

def get_plagas(request):
    planta=request.GET.get('planta')
    #print(planta)
    plaga= Datos.objects.all().filter(planta=planta).values_list('plaga')
    context={'plaga':plaga}
    #plagaselect=request.GET.get('plaga')
    #print(plagaselect)
    #print(plaga)
    return render(request, 'menu/plaga.html', context)

def display(request):
    planta = request.POST.get('planta')
    plaga = request.POST.get('plaga')

    results = Datos.objects.filter(planta=planta, plaga=plaga)
    context={"results":results}
    print(planta)
    print(plaga)
    print(results)
    return render(request, 'menu/display.html', context)
    



















#def boton(request):
    planta=request.GET.get('planta')
    plaga=request.GET.get('plaga')
    print(request)
    print(planta)
    print(plaga)
    context={}
    return render(request, 'menu/plaga.html', context)











#def capturarboton(request):
    chosenplant=''
    chosenplaga=''
    if request.method == 'POST':
        first_dropdown_value = request.POST.get('planta')
        chosenplant= first_dropdown_value
        second_dropdown_value = request.POST.get('plaga')
        chosenplaga= second_dropdown_value
    display= Datos.objects.all().filter(planta=chosenplant)
    display2=display.filter(plaga=chosenplaga)
    context={'display2':display2}
    return render(request, 'menu/plaga.html', context)


















#def boton(request):
    planta= request.GET.get('planta')
    plaga= request.GET.get('plaga')
    display= Datos.objects.all().filter(planta=planta)
    display2=display.filter(plaga=plaga)
    print(planta)
    print(plaga)
    context={'display':display}
    return render(request, 'menu/base.html' , context )



def home(request):
    return render(request, 'menu/base.html')