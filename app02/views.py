from django.shortcuts import render, redirect
from .models import Produtos
from .forms import ProdutoForm, ProfileForm
import os

def home(request):
    return render(request,'home.html')

def produto(request):
    produtos = Produtos.objects.filter(disponivel=True)
    return render(request, 'app02/produtos.html', {'produtos': produtos})

def add_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('produtos')
    else:
        form = ProdutoForm()
    return render(request, 'app02/add_produto.html', {'form': form})

def upload_profile(request):
    '''
    View para upload de foto de perfil
    '''
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'app02/upload_profile.html', {'form': form})