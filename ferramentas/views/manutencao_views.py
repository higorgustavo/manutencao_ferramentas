from django.shortcuts import render, redirect, get_object_or_404
from clientes.models import Cliente
from ..models import Ferramenta, Manutencao
from ..forms import ManutencaoForm
from django.contrib import messages


def detail_manutencao(request, id):
    manutencao = get_object_or_404(Manutencao, id=id)
    ferramenta = manutencao.ferramenta
    context = {
        'manutencao': manutencao,
        'ferramenta': ferramenta,
    }
    return render(request, "manutencoes/detail.html", context)


def create_manutencao(request, id):
    ferramenta = get_object_or_404(Ferramenta, id=id)

    if request.method == "GET":
        form = ManutencaoForm()
        context = {
            'ferramenta': ferramenta,
            'form': form,
        }
        return render(request, "manutencoes/create.html", context)

    elif request.method == "POST":
        form = ManutencaoForm(request.POST)
        if form.is_valid():
            manutencao = form.save(commit=False)
            manutencao.ferramenta = ferramenta
            manutencao.save()
            messages.add_message(request, messages.SUCCESS, "Manutenção registrada com sucesso")
            return redirect('/ferramenta/' + str(ferramenta.id))

        else:
            context = {
                'ferramenta': ferramenta,
                'form': form,
            }
            return render(request, "manutencoes/create.html", context)

