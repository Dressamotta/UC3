from django.shortcuts import render
from .models import Produto

def home(request):
    return render(request, 'app02/home.html')

def produtos(request):
    produtos = Produto.objects.all() # Cada objeto representa um produto
    return render(request, 'app02/produtos.html', {'produtos': produtos}) # Passa a lista de produtos para o template

def contatos(request):
    return render(request, 'app02/contatos.html')

# Create your views here.
