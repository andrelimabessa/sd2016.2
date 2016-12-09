from django.contrib import admin

#adicionado
from .models import Jogada
from .models import Posicao


# Register your models here.
class JogadaAdmin(admin.ModelAdmin):
    list_display=('autor', 'adversario', 'linha', 'coluna', 'created_date')
    list_filter=['autor']
    search_fields=['autor']
    class Meta:
        model = Jogada

admin.site.register(Jogada,JogadaAdmin)


class CriarTabuleiro(admin.ModelAdmin):
    list_display=('jogador', 'linha', 'coluna', 'status')
    list_filter=['jogador']
    search_fields=['jogador']
    class Meta:
        model = Posicao

    

admin.site.register(Posicao,CriarTabuleiro)

