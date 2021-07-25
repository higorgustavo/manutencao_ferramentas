from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Cliente
from .forms import ClienteForm
from ferramentas.models import Ferramenta, Manutencao
from django.contrib import messages


def list_clintes(request):
    termo = request.GET.get('termo')
    if termo:
        clientes = Cliente.objects.filter(nome__icontains=termo)
        paginator = Paginator(clientes, 10)
        page = request.GET.get('p')
        clientes = paginator.get_page(page)
    else:
        clientes = Cliente.objects.all()
        paginator = Paginator(clientes, 10)
        page = request.GET.get('p')
        clientes = paginator.get_page(page)

    context = {
        'clientes': clientes
     }
    return render(request, "clientes/list.html", context)


def detail_cliente(reqeust, id):
    cliente = get_object_or_404(Cliente, id=id)
    ferramentas = Ferramenta.objects.filter(cliente_id=cliente.id)
    context = {
        'cliente': cliente,
        'ferramentas': ferramentas
    }
    return render(reqeust, "clientes/detail.html", context)


def create_cliente(request):
    if request.method == "GET":
        form = ClienteForm()
        context = {
            'form': form,
        }
        return render(request, "clientes/create.html", context)

    elif request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            nome_cliente = str(request.POST.get("nome")).upper()
            messages.add_message(request, messages.SUCCESS,
                                 f'{nome_cliente} cadastrado(a) com sucesso!')
            return redirect('list_clintes')

        else:
            context = {
                "form": form
            }
            return render(request, "clientes/create.html", context)


def update_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(instance=cliente)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            messages.add_message(request, messages.SUCCESS, 'Dados alterados com sucesso!')
            return redirect('/cliente/' + str(cliente.id))
    context = {
        'cliente': cliente,
        'form': form,
    }
    return render(request, "clientes/updade.html", context)
