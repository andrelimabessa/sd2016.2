from django.contrib import admin
from .models import Jogada

class JogadaAdmin(admin.ModelAdmin):
	list_display=('autor', 'adversario', 'linha', 'coluna', 'created_date')
	class Meta:
		model = Jogada

admin.site.register(Jogada,JogadaAdmin)