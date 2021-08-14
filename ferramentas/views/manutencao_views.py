from django.shortcuts import render, redirect, get_object_or_404
from ..models import Ferramenta, Manutencao
from ..forms import ManutencaoForm, AgendamentoForm
from django.contrib import messages
from datetime import date


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
            if manutencao.status_manutencao == "Agendada" and manutencao.data_manutencao < date.today():
                manutencao.status_manutencao = "Atrasada"
            elif manutencao.status_manutencao == "Atrasada" and manutencao.data_manutencao == date.today():
                manutencao.status_manutencao = "Agendada"
                messages.add_message(request, messages.WARNING, 'Manutenção ATRASADA!!!')
            elif manutencao.status_manutencao == "Atrasada":
                messages.add_message(request, messages.WARNING, 'Manutenção ATRASADA!!!')
            else:
                messages.add_message(request, messages.SUCCESS, "Manutenção registrada com sucesso")
            manutencao.save()
            return redirect('/ferramenta/' + str(ferramenta.id))

        else:
            context = {
                'ferramenta': ferramenta,
                'form': form,
            }
            return render(request, "manutencoes/create.html", context)


def update_manutencao(request, id):
    manutencao = get_object_or_404(Manutencao, id=id)
    feramenta = manutencao.ferramenta
    form = ManutencaoForm(instance=manutencao)
    if request.method == "POST":
        form = ManutencaoForm(request.POST, instance=manutencao)
        if form.is_valid():
            manutencao = form.save(commit=False)
            manutencao.ferramenta = feramenta
            if manutencao.status_manutencao == "Agendada" and manutencao.data_manutencao < date.today():
                manutencao.status_manutencao = "Atrasada"
            elif manutencao.status_manutencao == "Atrasada" and manutencao.data_manutencao == date.today():
                manutencao.status_manutencao = "Agendada"
            elif manutencao.status_manutencao == "Atrasada":
                messages.add_message(request, messages.WARNING, 'Manutenção ATRASADA!!!')
            else:
                messages.add_message(request, messages.SUCCESS,
                                     'Manutenção ' + manutencao.status_manutencao + ' com Sucesso!')
            manutencao.save()
            return redirect('/ferramenta/' + str(feramenta.id))

    context = {
        'ferramenta': feramenta,
        'form': form
    }
    return render(request, "manutencoes/update.html", context)


def agendamento_rapido(request, id):
    ferramenta = get_object_or_404(Ferramenta, id=id)

    if request.method == "GET":
        form = AgendamentoForm()
        context = {
            'ferramenta': ferramenta,
            'form': form,
        }
        return render(request, "manutencoes/agendamento_rapido.html", context)

    elif request.method == "POST":
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            manutencao = form.save(commit=False)
            manutencao.ferramenta = ferramenta
            if manutencao.data_manutencao < date.today():
                manutencao.status_manutencao = "Atrasada"
            else:
                manutencao.status_manutencao = "Agendada"
            manutencao.save()
            messages.add_message(request, messages.SUCCESS, "Manutenção Agendada com sucesso!")
            return redirect('/cliente/' + str(ferramenta.cliente.id))

        else:
            context = {
                'ferramenta': ferramenta,
                'form': form,
            }
            return render(request, "manutencoes/agendamento_rapido.html", context)
