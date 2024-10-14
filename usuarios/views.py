from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

def ver_usuarios(request):
    if request.method =='GET':
         return render(request,'index.html')
     
    elif request.method == "POST":    
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        idade = request.POST.get('idade')
        
        pessoa = Pessoa(nome=nome, email=email, idade=idade)
        pessoa.save()
        
        
        return HttpResponse('Cadastrado com sucesso')


