from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from ..models import Ferramenta, Manutencao
from ..forms import ManutencaoForm, AgendamentoForm
from ..filters import ManutencaoFilter
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
                messages.add_message(request, messages.ERROR, 'Manutenção ATRASADA!!!')
            elif manutencao.status_manutencao == "Atrasada" and manutencao.data_manutencao >= date.today():
                manutencao.status_manutencao = "Agendada"
                messages.add_message(request, messages.SUCCESS,
                                     'Manutenção Agendada com Sucesso!')
            elif manutencao.status_manutencao == "Atrasada":
                messages.add_message(request, messages.ERROR, 'Manutenção ATRASADA!!!')
            else:
                messages.add_message(request, messages.SUCCESS,
                                     'Manutenção ' + manutencao.status_manutencao + ' com Sucesso!')
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
                messages.add_message(request, messages.ERROR, 'Manutenção ATRASADA!!!')
            elif manutencao.status_manutencao == "Atrasada" and manutencao.data_manutencao >= date.today():
                manutencao.status_manutencao = "Agendada"
                messages.add_message(request, messages.SUCCESS,
                                     'Manutenção Agendada com Sucesso!')
            elif manutencao.status_manutencao == "Atrasada":
                messages.add_message(request, messages.ERROR, 'Manutenção ATRASADA!!!')
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
                messages.add_message(request, messages.ERROR, "Manutenção ATRASADA!!!")
            else:
                manutencao.status_manutencao = "Agendada"
                messages.add_message(request, messages.SUCCESS, "Manutenção Agendada com sucesso!")
            manutencao.save()
            return redirect('/cliente/' + str(ferramenta.cliente.id))

        else:
            context = {
                'ferramenta': ferramenta,
                'form': form,
            }
            return render(request, "manutencoes/agendamento_rapido.html", context)


def list_agendadas(request):
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    status = "Agendadas"
    if data_inicial and data_final:
        manutencoes = Manutencao.objects.filter(status_manutencao="Agendada",
                                                data_manutencao__range=[data_inicial, data_final])
        manutencao_filter = ManutencaoFilter(request.GET, queryset=manutencoes)
        manutencoes = manutencao_filter.qs
        paginator = Paginator(manutencoes, 10)
        page = request.GET.get('p')
        manutencoes = paginator.get_page(page)
    else:
        manutencoes = Manutencao.objects.filter(status_manutencao="Agendada")
        manutencao_filter = ManutencaoFilter(request.GET, queryset=manutencoes)
        manutencoes = manutencao_filter.qs
        paginator = Paginator(manutencoes, 10)
        page = request.GET.get('p')
        manutencoes = paginator.get_page(page)
    context = {
        'manutencoes': manutencoes,
        'status': status,
        'manutencao_filter': manutencao_filter,
        'data_inicial': data_inicial,
        'data_final': data_final
    }
    return render(request, "manutencoes/list.html", context)


def list_agendadas_hoje(request):
    manutencoes = Manutencao.objects.filter(status_manutencao="Agendada", data_manutencao=date.today())
    status = "Agendadas para Hoje"
    manutencao_filter = ManutencaoFilter(request.GET, queryset=manutencoes)
    manutencoes = manutencao_filter.qs
    paginator = Paginator(manutencoes, 10)
    page = request.GET.get('p')
    manutencoes = paginator.get_page(page)
    context = {
        'manutencoes': manutencoes,
        'status': status,
        'manutencao_filter': manutencao_filter
    }
    return render(request, "manutencoes/list.html", context)


def list_atrasadas(request):
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    status = "Atrasadas"
    if data_inicial and data_final:
        manutencoes = Manutencao.objects.filter(status_manutencao="Atrasada",
                                                data_manutencao__range=[data_inicial, data_final])
        manutencao_filter = ManutencaoFilter(request.GET, queryset=manutencoes)
        manutencoes = manutencao_filter.qs
        paginator = Paginator(manutencoes, 10)
        page = request.GET.get('p')
        manutencoes = paginator.get_page(page)
    else:
        manutencoes = Manutencao.objects.filter(status_manutencao="Atrasada")
        manutencao_filter = ManutencaoFilter(request.GET, queryset=manutencoes)
        manutencoes = manutencao_filter.qs
        paginator = Paginator(manutencoes, 10)
        page = request.GET.get('p')
        manutencoes = paginator.get_page(page)
    context = {
        'manutencoes': manutencoes,
        'status': status,
        'manutencao_filter': manutencao_filter,
        'data_inicial': data_inicial,
        'data_final': data_final
    }
    return render(request, "manutencoes/list.html", context)


def list_concluidas(request):
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    status = "Concluídas"
    if data_inicial and data_final:
        manutencoes = Manutencao.objects.filter(status_manutencao="Concluída",
                                                data_manutencao__range=[data_inicial, data_final])
        manutencao_filter = ManutencaoFilter(request.GET, queryset=manutencoes)
        manutencoes = manutencao_filter.qs
        paginator = Paginator(manutencoes, 10)
        page = request.GET.get('p')
        manutencoes = paginator.get_page(page)
    else:
        manutencoes = Manutencao.objects.filter(status_manutencao="Concluída")
        manutencao_filter = ManutencaoFilter(request.GET, queryset=manutencoes)
        manutencoes = manutencao_filter.qs
        paginator = Paginator(manutencoes, 10)
        page = request.GET.get('p')
        manutencoes = paginator.get_page(page)
    context = {
        'manutencoes': manutencoes,
        'status': status,
        'manutencao_filter': manutencao_filter,
        'data_inicial': data_inicial,
        'data_final': data_final
    }
    return render(request, "manutencoes/list.html", context)


def list_canceladas(request):
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    status = "Canceladas"
    if data_inicial and data_final:
        manutencoes = Manutencao.objects.filter(status_manutencao="Cancelada",
                                                data_manutencao__range=[data_inicial, data_final])
        manutencao_filter = ManutencaoFilter(request.GET, queryset=manutencoes)
        manutencoes = manutencao_filter.qs
        paginator = Paginator(manutencoes, 10)
        page = request.GET.get('p')
        manutencoes = paginator.get_page(page)
    else:
        manutencoes = Manutencao.objects.filter(status_manutencao="Cancelada")
        manutencao_filter = ManutencaoFilter(request.GET, queryset=manutencoes)
        manutencoes = manutencao_filter.qs
        paginator = Paginator(manutencoes, 10)
        page = request.GET.get('p')
        manutencoes = paginator.get_page(page)
    context = {
        'manutencoes': manutencoes,
        'status': status,
        'manutencao_filter': manutencao_filter,
        'data_inicial': data_inicial,
        'data_final': data_final
    }
    return render(request, "manutencoes/list.html", context)
