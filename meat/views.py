from django.shortcuts import render, redirect
from meat.models import *
from random import randint
from django.templatetags.static import static
from meat.forms import Form_meats
# Create your views here.
# this was created for starting the first product
def meats(request):
    rand = randint(0, 2000)
    al1 = Products.objects.create(name = 'Carne', description = 'Carne de ternera', sku = rand, price = 2000)
    context = {
        'meat': al1
    }
    return render(request, 'meat/meats.html', context=context)


def list_of_meats(request):

    all = Products.objects.all()

    context ={
        'list' : all
    }
    return render(request,'meat/meats.html', context = context)

def form_meat(request):
    if request.method == 'POST':
        form = Form_meats(request.POST)
        if form.is_valid():
            Products.objects.create (
			     name = form.cleaned_data['name'],
			     price = form.cleaned_data['price' ],
                 description = form.cleaned_data['description'],
                 stock = form.cleaned_data['stock']
							)
        return redirect(list_of_meats)
    elif request.method == 'GET':
        form = Form_meats
        context = {
            'form': form
        }
    return render(request, 'meat/create_meats.html', context=context)


def update_meats(request, pk):
    if request.method == 'POST':
        form = Form_meats(request.POST)
        if form.is_valid():
            product = Products.objects.get(id=pk)
            product.name = form.cleaned_data['name']
            product.price = form.cleaned_data['price']
            product.description = form.cleaned_data['description']
            product.stock = form.cleaned_data['stock']
            product.save()

            return redirect(list_of_meats)

    elif request.method == 'GET':
        product = Products.objects.get(id=pk)

        form = Form_meats (initial={
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'stock': product.stock})
        context = {'form': form}
        return render(request, 'meat/update_meats.html', context=context)




def delete_meats(request, pk):
    if request.method == 'GET':
        product = Products.objects.get(pk=pk)
        context = {'product': product}
        return render(request, 'meat/delete_meats.html', context=context)
    elif request.method == 'POST':
        product = Products.objects.get(pk=pk)
        product.delete()
        return redirect(list_of_meats)
