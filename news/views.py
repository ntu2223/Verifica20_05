from django.shortcuts import render,redirect
from .forms import BlogPostModelForm
from .models import BlogPostModel

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_list_or_404, get_object_or_404

def home(request): 
    #api_list = ['lista giornalisti','lista articoli']
    #context = {
   #     'cmd_list': cmd_list,
    #}
    return render(request, "home.html", context)

    class listaArticoliView(ListView):
    model = BlogPostModel #modello dei dati da utilizzare 
    template_name = "news/articoli.html" 

    class listaGiornalistiView(ListView):
    model = BlogPostModel #modello dei dati da utilizzare 
    template_name = "news/giornalisti.html" 



# Create your views here.
