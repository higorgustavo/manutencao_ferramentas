from django.shortcuts import render, redirect, get_object_or_404
from clientes.models import Cliente
from ..models import Ferramenta, Manutencao
from ..forms import FerramentaForm
from django.contrib import messages
from datetime import date


def detail_ferramenta(reqeust, id):
    ferramenta = get_object_or_404(Ferramenta, id=id)
    manutencoes = Manutencao.objects.filter(ferramenta_id=ferramenta.id)
    cliente = ferramenta.cliente
    # for manutencao in manutencoes:
    #     if manutencao.status_manutencao == "Agendada" and manutencao.data_manutencao < date.today():
    #         manutencao.status_manutencao = "Atrasada"
    #         Manutencao.objects.bulk_update(manutencoes, ['status_manutencao'])
    #     if manutencao.status_manutencao == "Atrasada" and manutencao.data_manutencao >= date.today():
    #         manutencao.status_manutencao = "Agendada"
    #         Manutencao.objects.bulk_update(manutencoes, ['status_manutencao'])
    context = {
        'cliente': cliente,
        'ferramenta': ferramenta,
        'manutencoes': manutencoes,
    }
    return render(reqeust, "ferramentas/detail.html", context)


def create_ferramenta(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == "GET":
        form = FerramentaForm()
        context = {
            'cliente': cliente,
            'form': form,
        }
        return render(request, "ferramentas/create.html", context)

    elif request.method == "POST":
        form = FerramentaForm(request.POST)
        if form.is_valid():
            ferramenta = form.save(commit=False)
            ferramenta.cliente = cliente
            ferramenta.save()
            messages.add_message(request, messages.SUCCESS, "Ferramenta cadastrada com sucesso")
            return redirect('/cliente/' + str(cliente.id))

        else:
            context = {
                'cliente': cliente,
                'form': form,
            }
            return render(request, "ferramentas/create.html", context)


def update_ferramenta(request, id):
    ferramenta = get_object_or_404(Ferramenta, id=id)
    cliente = ferramenta.cliente
    form = FerramentaForm(instance=ferramenta)
    if request.method == "POST":
        form = FerramentaForm(request.POST, instance=ferramenta)
        if form.is_valid():
            ferramenta = form.save(commit=False)
            ferramenta.cliente = cliente
            ferramenta.save()
            messages.add_message(request, messages.SUCCESS, 'Dados alterados com sucesso')
            return redirect('/cliente/' + str(cliente.id))

    context = {
        'cliente': cliente,
        'form': form
    }
    return render(request, "ferramentas/update.html", context)



