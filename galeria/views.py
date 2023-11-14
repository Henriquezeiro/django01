from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def imagem(request):
    return render(request, 'imagem.html')