from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime

# vista sin template
def current_datetime(request):
    now=datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# vista con templates
def index(request):
    template = loader.get_template('miapp/index.html')
    context = {
        'paises':["chile","argentina","peru"],
        'nombre':'hola mundo'
    }
    return HttpResponse(template.render(context, request))  
