# -*- coding: utf-8 -*-
from django import template
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render_to_response, get_object_or_404
from servico.models import *
from locale import setlocale, currency, LC_ALL

register = template.Library()

@register.simple_tag
def funcionarios_cargo(request, servico, cargo):
    qtd = servico.quantidade_cargo(cargo)
    qtd_dias_previsto = servico.quantidade_dias_previstos
    qtd_dias_executados = servico.quantidade_dias_executados()
    producao = servico.producao_por_funcionario(cargo)
    producao_dia = producao / qtd_dias_previsto
    producao_total = producao * qtd
    
    try:
       setlocale(LC_ALL,'pt_BR.UTF-8')
    except:
       setlocale(LC_ALL,'portuguese')

    producao = u"R$ " + str(currency(producao, grouping=True, symbol=False))         
    producao_dia = u"R$ " + str(currency(producao_dia, grouping=True, symbol=False))     
    producao_total = u"R$ " + str(currency(producao_total, grouping=True, symbol=False))        
   
    return {
        'cargo': cargo,
        'qtd': qtd,
        'qtd_dias_previsto': qtd_dias_previsto,
        'qtd_dias_executados': qtd_dias_executados,
        'producao_funcionario': producao,
        'producao_dia': producao_dia,
        'producao_total': producao_total
    }

register.inclusion_tag('admin/funcionarios_cargo.html')(funcionarios_cargo)

@register.simple_tag
def funcionarios(request, servico, funcionario):
    datas = []
    presencas = []
    for data in servico.datas_executadas():
        datas.append(data)
    for presenca in servico.presencas_funcionario(funcionario):
        presencas.append(presenca)
    return {
        'funcionario': funcionario,
        'datas': datas,
        'presencas': presencas
    }

register.inclusion_tag('admin/funcionario.html')(funcionarios)

@register.simple_tag
def funcionarios_presenca(request, servico, funcionario):
    datas = []
    presencas = []
    for data in servico.datas(funcionario):
        datas.append(data)
    for presenca in servico.presencas_funcionario_edit(funcionario):
        presencas.append(presenca)
    return {
        'funcionario': funcionario,
        'datas': datas,
        'presencas': presencas
    }

register.inclusion_tag('admin/funcionario_presenca.html')(funcionarios_presenca)

@register.simple_tag
def funcionarios_impressao(request, servico, funcionario):
    presencas = []
    for presenca in servico.presencas_funcionario_impressao(funcionario):
        presencas.append(presenca)
    return {
        'funcionario': funcionario,
        'presencas': presencas
    }

register.inclusion_tag('admin/funcionario_impressao.html')(funcionarios_impressao)


@register.simple_tag
def funcionarios_producao(request, funcionario, mes, ano):
    qtd_faltas_justificadas = funcionario.quantidade_faltas_justificadas_mes(mes, ano)
    qtd_faltas_nao_justificadas = funcionario.quantidade_faltas_nao_justificadas_mes(mes, ano)
    producao = funcionario.producao(mes, ano)

    try:
       setlocale(LC_ALL,'pt_BR.UTF-8')
    except:
       setlocale(LC_ALL,'portuguese')

    producao = u"R$ " + str(currency(producao, grouping=True, symbol=False))
    
    return {
        'qtd_faltas_justificadas': qtd_faltas_justificadas,
        'qtd_faltas_nao_justificadas': qtd_faltas_nao_justificadas,
        'producao': producao
    }

register.inclusion_tag('admin/funcionarios_producao.html')(funcionarios_producao)

@register.simple_tag
def producao(request, servico):
    cargos  = []

    producao_final_total = 0.0
    for funcionario in servico.funcionarios.all():
        if funcionario.cargo() not in cargos:
            cargos.append(funcionario.cargo())
        if servico.valido():
            vlr_efetivo = float(servico.producao_por_funcionario(funcionario.cargo()))
            desconto = float(servico.desconto(funcionario))
            #rateio_a_receber = float(servico.rateio_a_receber(funcionario))
            rateio = RateioFuncionario.objects.get(servico = servico, funcionario = funcionario)
            rateio_a_receber = float(rateio.valor)
            qtd_dias_previsto = servico.quantidade_dias_previstos
            qtd_dias_executados = servico.quantidade_dias_executados()
            if qtd_dias_executados > qtd_dias_previsto:
                rateio_a_receber = 0.0
            valor = (vlr_efetivo - desconto + rateio_a_receber)
            if valor < 0.0:
                valor = 0.0
            if funcionario.quantidade_faltas_nao_justificadas_mes(servico.periodo.mes, servico.periodo.ano) > 2 :
                valor = 0.0
            producao_final_total = producao_final_total + valor 
    valor_total = servico.valor_total
    try:
       setlocale(LC_ALL,'pt_BR.UTF-8')
    except:
       setlocale(LC_ALL,'portuguese')

    valor_pago = u"R$ " + str(currency(producao_final_total, grouping=True, symbol=False))
    valor_total = u"R$ " + str(currency(valor_total, grouping=True, symbol=False))   

    return {
        'servico': servico,
        'valor_pago': valor_pago,
        'valor_total': valor_total,
        'cargos': cargos
    } 

register.inclusion_tag('admin/producao_impressao.html')(producao)

@register.simple_tag
def calculo_producao(request, servico, funcionario):
    qtd_presencas_p = servico.qtd_presencas_p(funcionario)
    qtd_presencas_mp = servico.qtd_presencas_mp(funcionario)
    qtd_presencas_f = servico.qtd_presencas_f(funcionario)
    vlr_efetivo = float(servico.producao_por_funcionario(funcionario.cargo()))
    desconto = float(servico.desconto(funcionario))
    vlr_rateio = float(servico.rateio_funcionario(funcionario))
    mensagem = ""
    rateio_manual = False
    qtd_dias_previsto = servico.quantidade_dias_previstos
    qtd_dias_executados = servico.quantidade_dias_executados()
    if servico.valido():
        #rateio_a_receber = float(servico.rateio_a_receber(funcionario))
        rateio = RateioFuncionario.objects.get(servico = servico, funcionario = funcionario)
        rateio_a_receber = float(rateio.valor)
        if rateio.manual:
            rateio_manual = True
        if qtd_dias_executados > qtd_dias_previsto:
            rateio_a_receber = 0.0
        producao_final = vlr_efetivo - desconto + rateio_a_receber
        if producao_final < 0.0:
            producao_final = 0.0
        qtd_faltas = funcionario.quantidade_faltas_nao_justificadas_mes(servico.periodo.mes, servico.periodo.ano)
        if  qtd_faltas > 2 :
            producao_final = 0.0
            rateio_a_receber = 0.0
            mensagem = u"<br>Produção mensal zerada por faltas não justificadas (%s falta(s))"%(qtd_faltas)
    else:
        rateio_a_receber = 0
        vlr_rateio = 0
        producao_final = 0
        mensagem = u"<br>Produção mensal zerada por exceder em 30% o tempo previsto"

    try:
       setlocale(LC_ALL,'pt_BR.UTF-8')
    except:
       setlocale(LC_ALL,'portuguese')

    vlr_efetivo = u"R$ " + str(currency(vlr_efetivo, grouping=True, symbol=False))
    desconto = u"R$ " + str(currency(desconto, grouping=True, symbol=False))
    vlr_rateio = u"R$ " + str(currency(vlr_rateio, grouping=True, symbol=False))
    rateio_a_receber = u"R$ " + str(currency(rateio_a_receber, grouping=True, symbol=False))
    producao_final = u"R$ " + str(currency(producao_final, grouping=True, symbol=False))
    producao_final = producao_final + mensagem

    return {
        'funcionario': funcionario,
        'qtd_presencas_p': qtd_presencas_p,
        'qtd_presencas_mp': qtd_presencas_mp,
        'qtd_presencas_f': qtd_presencas_f,
        'vlr_efetivo': vlr_efetivo,
        'desconto': desconto,
        'vlr_rateio': vlr_rateio,
        'rateio_a_receber': rateio_a_receber,
        'producao_final': producao_final,
        'rateio_manual': rateio_manual
    }

register.inclusion_tag('admin/producao_funcionario.html')(calculo_producao)