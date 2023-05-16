#from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .models import DadosSaresp

##Funções globais

def pegaEscolas():
    escolas = DadosSaresp.objects.raw("SELECT DISTINCT codesc, escola, 1 as id_reg FROM dados_saresp")
    return escolas

def IndexView(request):
    return render(request, 'index.html')

def EscolasView(request):
<<<<<<< HEAD
    escolano = DadosSaresp.objects.raw("SELECT DISTINCT ano_saresp, escola, 1 as id_reg FROM dados_saresp")
    return render(request, 'escolas.html', {'escolano': escolano})

def EscolasView(request):
=======
>>>>>>> b73c7354892a3a035c8c98a81650e194ccba4166
    escolas = pegaEscolas()
    return render(request, 'escolas.html', {'escolas': escolas})

def EscolaView(request, codesc):
    escolas = pegaEscolas()
    escola = DadosSaresp.objects.raw("SELECT serie_ano, AVG(porc_cert_lp) AS porc_cert_lp, AVG(porc_cert_mat) AS porc_cert_mat, AVG(porc_cert_cie) AS porc_cert_cie, 1 as id_reg FROM dados_saresp WHERE codesc = " + str(codesc) + " GROUP BY serie_ano")
    return render(request, 'escola.html', {'escola': escola, 'escolas': escolas})

def DashView(request):
    return render(request, 'dash.html')
