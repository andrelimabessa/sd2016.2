from django.shortcuts import render
from django.shortcuts import redirect
from .forms import JogadaForm
from .formsTabuleiro import TabuleiroForm
from django.utils import timezone
import random
from .models import Posicao

# Create your views here.
def post_list(request):
    
    if request.method == "POST":
        form = JogadaForm(request.POST)
        if form.is_valid():
            jogada = form.save(commit=False)
            jogada.autor = request.user
            jogada.created_date = timezone.now()
            jogada.save()

            posicao = Posicao.objects.filter(linha=jogada.linha, coluna=jogada.coluna, jogador=jogada.adversario, status=1)
            if not posicao:
                print("Errou")
                context = {'msgError': ' Você Errou.'}
                return render(request, 'tabuleiro.html', context)
            else:
                Posicao.objects.filter(linha=jogada.linha, coluna=jogada.coluna, jogador=jogada.adversario).update(status=0)
                print("Acertou")
                context = {'msgAcerto': ' Você Acertou.'}
                return render(request, 'tabuleiro.html', context)
            ##return redirect('tabuleiro/')
    else:
        form = JogadaForm()

    return render(request, 'post_list.html', {'form': form})

def post_tabuleiro(request):
    return render(request, 'tabuleiro.html')

def criar_tabuleiro(request):
    Posicao.objects.filter(jogador=request.user).delete()
    for i in range(2):
        existe = False
        linha = random.randint(0,4)
        coluna = random.randint(0,4)
        posicoes = Posicao.objects.filter(jogador=request.user)
        for pos in posicoes:
            if pos.linha == linha and pos.coluna == coluna:
                existe=True
                break
        if existe:
            i-=1
        else:
            form = TabuleiroForm()
            posicao = form.save(commit=False)
            posicao.jogador = request.user
            posicao.linha = linha
            posicao.coluna = coluna
            posicao.status = 1
            posicao.save()
    return redirect('teste/')

   