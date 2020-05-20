
from django.urls import path
from . import views listaGiornalistiView,listaArticoliView
app_name = 'news'
urlpatterns = [ 
    path('', views.home, name='home')

    path('lista-articoli', listaPostView.as_view(), name='lista_articoli'),
    path('lista-giornalisti', listaGiornalistiView.as_view(), name='lista_giornalisti'),

]