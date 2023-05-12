from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView, name='dados-home'),
    path('escolas/<int:codesc>', views.EscolaView, name='escola-home'),
    path('escolas', views.EscolasView, name='escolas-home')
]
