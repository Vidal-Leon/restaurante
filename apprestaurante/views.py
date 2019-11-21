from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib import messages
from .forms import MenuForm
from apprestaurante.models import Menu, Plato, Empleado, Venta, Cliente
from django.shortcuts import redirect

from django.db.models import Q

def listar_platos(request):
    platos = Plato.objects.all()
    return render(request, 'apprestaurante/menu_editar.html', {'platos':platos})

def menu_nuevo(request):

    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            plato = Plato.objects.create(nombre=form.cleaned_data['nombre'], descripcion = form.cleaned_data['descripcion'])
            for plato_id in request.POST.getlist('plato'):
                menu = Menu(plato_id=plato_id)
                menu.save()

            messages.add_message(request, messages.SUCCESS, 'Menu guardado Exitosamente!')

    else:

        form = MenuForm()

    return render(request, 'apprestaurante/listar_platos.html', {'form': form})

def detalle_menus(request, pk):

    detalle_menus = get_list_or_404(Menu.objects.all(), menu=pk) #get_object_or_404(Ejercito, pk=pk)
    return render(request, 'mazos/detalle_menus.html', {'detalle_menus': detalle_menus})
