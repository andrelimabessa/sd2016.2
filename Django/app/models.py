from django.db import models

#Adicionado
from django.utils import timezone

# Create your models here.

#Adicionado
class Jogada(models.Model):
    autor = models.ForeignKey('auth.User', related_name="autor")
    adversario = models.ForeignKey('auth.User', related_name='adversario')
    linha = models.CharField(max_length=2)
    coluna = models.CharField(max_length=2)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "Jogada de " + self.autor.username + " contra " + self.adversario.username + " realizada no dia " + self.created_date.strftime('%d %B %Y') + " : linha " + self.linha + ", coluna " + self.coluna
    
