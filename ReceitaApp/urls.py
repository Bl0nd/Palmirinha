from django.urls import path
from ReceitaApp import views

# 'caminho', nome da view(def), nome url
urlpatterns = [
    path('', views.index, name ='index'),
    path('receitas/', views.receitas, name ='receitas')
]