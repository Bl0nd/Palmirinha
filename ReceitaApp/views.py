from django.shortcuts import render
from ReceitaApp.models import Receita

# Create your views here.
def index(request):
    #ações daminha view..
    return render(request, 'index.html')

def receitas(request):
#Buscar as receitas no banco
    lista_receitas = Receita.objects.all()

    #Dicionario contendo as informações que iremos usar no template
    context = {
        'receitas': lista_receitas,
    }
    return render(request, 'receitas.hmtl', context)