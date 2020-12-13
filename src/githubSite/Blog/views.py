from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

from .models import Article
# Create your views here.

class ArticleListView(ListView):
    template_name = 'articles/list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'articles/detail.html'
    queryset = Article.objects.all()

