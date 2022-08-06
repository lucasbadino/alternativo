from django.shortcuts import render, redirect
from random import randint
from panificacion.models import Panes
from panificacion.forms import Formulario_panes
from django.templatetags.static import static


def panes(request):
    rand = randint(0, 2000)
    al1 = Panes.objects.create(name = 'Pan Frances', description = 'baguette', sku = rand, price = 50)
    context = {
        'pan': al1
    }
    return render(request, 'panes.html', context=context)


def lista_panes(request):

    all = Panes.objects.all()

    context ={
        'lista' : all
    }
    return render(request,'panes.html', context = context)

def form_panes(request):
    if request.method == 'POST':
        form = Formulario_panes(request.POST)
        if form.is_valid():
            Panes.objects.create (
			     name = form.cleaned_data['name'],
			     price = form.cleaned_data['price' ],
                 description = form.cleaned_data['description'],
                 stock = form.cleaned_data['stock']
							)
        return redirect(lista_panes)
    elif request.method == 'GET':
        form = Formulario_panes
        context = {
            'form': form
        }
    return render(request, 'crear_panes.html', context=context)