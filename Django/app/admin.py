from django.contrib import admin

#adicionado
from .models import Jogada

# Register your models here.
class JogadaAdmin(admin.ModelAdmin):
    list_display=('autor', 'adversario', 'linha', 'coluna', 'created_date')
    list_filter=['autor']
    search_fields=['autor']
    class Meta:
        model = Jogada

admin.site.register(Jogada,JogadaAdmin)
