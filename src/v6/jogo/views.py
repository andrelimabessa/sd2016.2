from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from jogo.models import Jogo
from jogada.models import Jogada

from utils.batalha import BatalhaNaval

class JogoForm(ModelForm):
    class Meta:
        model = Jogo
        fields = ['jogador1', 'jogador2', 'jogadasMaxima']

@login_required
def jogo_list(request, template_name='jogo/jogo_list.html'):
    jogo = Jogo.objects.all()
    data = {}
    data['object_list'] = jogo
    return render(request, template_name, data)

@login_required
def jogo_jogadas(request, pk, template_name='jogada/jogada_list.html'):    
    return redirect('jogada:jogada_list', pk)

@login_required
def jogo_create(request, template_name='jogo/jogo_form.html'):
    form = JogoForm(request.POST or None)
    if form.is_valid():
        jogo = form.save()        
        # registra tabuleiro com configurações
        BatalhaNaval().tabuleiroGerar(jogo)        

        return redirect('jogo:jogo_list')
    return render(request, template_name, {'form':form})

@login_required
def jogo_update(request, pk, template_name='jogo/jogo_form.html'):
    jogo= get_object_or_404(Jogo, pk=pk)
    form = JogoForm(request.POST or None, instance=jogo)
    if form.is_valid():
        form.save()
        return redirect('jogo:jogo_list')
    return render(request, template_name, {'form':form})

def jogo_delete(request, pk, template_name='jogo/jogo_confirm_delete.html'):
    jogo= get_object_or_404(Jogo, pk=pk)    
    if request.method=='POST':
        jogo.delete()
        return redirect('jogo:jogo_list')
    return render(request, template_name, {'object':jogo})