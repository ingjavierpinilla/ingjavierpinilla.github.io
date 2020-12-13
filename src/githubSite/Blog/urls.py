from django.urls import path
from .views import (
    ArticleDetailView,
    ArticleListView
)

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name ='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name ='article_detail') #pk = primary key

]