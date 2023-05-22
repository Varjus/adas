from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView, name='dados-home'),
    path('dados/escolas/<int:codesc>', views.EscolaView, name='escola-home'),
    path('escolas', views.EscolasView, name='escolas-home'),

   ## path('dados/ano/<int:codesc>', views.anosView, name='escola-home'),
    path('dash', views.DashView, name='escolas-dash'),
    path('dashlp', views.DashPView, name='escolas-dashp'),
    path('dashc', views.DashCView, name='escolas-dashc'),
     path('dashg', views.DashGView, name='escolas-dashg'),
    path('sobre', views.SobreView, name='sobre'),
]
