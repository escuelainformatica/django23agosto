1) Creando un proyecto de Django.

2) crear una aplicacion

Usando la linea de comando:

```python
python .\manage.py startapp miapp
```

3) Dentro de la carpeta del proyecto, modificar el settings.py y agregar la app

```python
INSTALLED_APPS = [
    # ....
    'miapp.apps.MiappConfig', # cambiar por el nombre de proyecto usado
    # ....
]
```

4) En la carpeta de la aplicacion, editar views.py

```python
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('miapp/index.html')
    context = {
        'paises':["chile","argentina","peru"],
        'nombre':'hola mundo'
    }
    return HttpResponse(template.render(context, request))
```

4.1) Donde def index es el nombre de la funcion (puede poner cualquier nombre)

5) En el paso anterior se usa el template en la carpeta /templates/miapp/index.hml
Cree ese archivo e indique un contenido web.

```html
<h1>ofofdofdofd</h1>

<h2>esto es un template</h2>

El nombre se llama <b>{{ nombre|upper }}</b><br>
El nombre se llama <b>{{ nombre|lower }}</b><br>

<ul>
    {% for pais in paises %}
    <li>{{ pais|capfirst }}</li>
    {% endfor %}

</ul>
```


