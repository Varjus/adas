#from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import DadosSaresp

##Funções globais

def pegaEscolas():
    escolas = DadosSaresp.objects.raw("SELECT DISTINCT codesc, escola, 1 as id_reg FROM dados_saresp ORDER BY escola")
    return escolas

def IndexView(request):
    return render(request, 'index.html')

def EscolasView(request):
    escolas = pegaEscolas()
    return render(request, 'escolas.html', {'escolas': escolas})

def EscolaView(request, codesc):
    escolas = pegaEscolas()
    escola = DadosSaresp.objects.raw("SELECT serie_ano, AVG(porc_cert_lp) AS porc_cert_lp, AVG(porc_cert_mat) AS porc_cert_mat, AVG(porc_cert_cie) AS porc_cert_cie, 1 as id_reg FROM dados_saresp WHERE codesc = " + str(codesc) + " GROUP BY serie_ano")
    return render(request, 'escola.html', {'escola': escola, 'escolas': escolas})

def DashView(request):
    escolas = DadosSaresp.objects.raw("SELECT codesc, escola, serie_ano, ano_saresp, AVG(porc_cert_lp) AS porc_cert_lp, AVG(porc_cert_mat) AS porc_cert_mat, AVG(porc_cert_cie) AS porc_cert_cie, 1 as id_reg FROM dados_saresp WHERE codesc IN (SELECT DISTINCT codesc FROM dados_saresp) GROUP BY serie_ano, escola, ano_saresp, codesc")
    return render(request, 'dash.html', {'escolas': escolas})

def SobreView(request):
    return render(request, 'sobre.html')
