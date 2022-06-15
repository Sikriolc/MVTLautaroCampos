from html.entities import html5
from django.template import Template,Context,loader
from Familiares.models import Familia
from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    
	return HttpResponse("<h1>Inicio MVT Campos Lautaro</h1>  <h3>Datos bd en => http://127.0.0.1:8000/Familia/ </h3>")



def familias(request):
    fam=Familia.objects.all().values()
    template=loader.get_template('index.html')
    context={
        'Familia': fam,
    }
    return HttpResponse(template.render(context,request))