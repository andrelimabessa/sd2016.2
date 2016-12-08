from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.forms import ModelForm
from django.core import validators
from django.contrib import messages 

from jogo.models import Jogo
from jogada.models import Jogada
from utils.batalha import BatalhaNaval

class JogadaForm(ModelForm):
    class Meta:
        model = Jogada
        fields = ['linha', 'coluna']

@login_required
def jogada_list(request, jogoId, template_name='jogada/jogada_list.html'):
    jogada = Jogada.objects.filter(jogo_id=jogoId)
    data = {}
    data['object_list'] = jogada
    data['jogoId'] = int(jogoId)    

    jogo = Jogo.objects.get(id=jogoId)
    data['jogo'] = jogo

    return render(request, template_name, data)

@login_required
def jogada_create(request, jogoId, template_name='jogada/jogada_form.html'):    
    jogoAtual = Jogo.objects.get(pk=jogoId)     # obtém jogo da url
    form = JogadaForm(request.POST or None)

    if form.is_valid():
        form.registro = timezone.now()
        jogada = form.save(commit=False)
        jogada.jogo = jogoAtual                 # define jogo da url
        jogada.autor = request.user             # define autor usuário logado        
        resultado = BatalhaNaval().permiteJogada(jogada)
        if resultado == "":
            jogada.save()
            BatalhaNaval().atualizar(jogada)            

            return redirect('jogada:jogada_list', jogoId)
        else:
            messages.error(request, resultado)

    return render(request, template_name, {'form':form, 'jogoAtual': jogoAtual, 'autor': request.user.username})

@login_required
def jogada_update(request, pk, jogoId, template_name='jogada/jogada_form.html'):
    jogada= get_object_or_404(Jogada, pk=pk)
    form = JogadaForm(request.POST or None, instance=jogada)
    if form.is_valid():
        form.save()
        return redirect('jogada:jogada_list', jogoId)
    return render(request, template_name, {'form':form})

@login_required
def jogada_delete(request, pk, template_name='jogada/jogada_confirm_delete.html'):
    jogada= get_object_or_404(Jogada, pk=pk)    
    if request.method=='POST':
        jogada.delete()
        return redirect('jogada:jogada_list')
    return render(request, template_name, {'object':jogada})