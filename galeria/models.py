from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import os

def get_upload_path(instance, filename):
    nome_objeto = instance.nome

    caminho = f"fotos/{nome_objeto}/{filename}"

    return caminho

class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]

    nome = models.CharField( max_length=100, null= False, blank = False )
    legenda = models.CharField( max_length=150, null = False, blank=False )
    categoria = models.CharField( max_length=100, choices=OPCOES_CATEGORIA, default='' )
    descricao = models.TextField( null=False, blank= False )
    foto = models.ImageField(upload_to=get_upload_path, blank=True)
    publicada = models.BooleanField( default= False )
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(
        to=User,
        on_delete= models.SET_NULL,
        null= True,
        blank=False,
        related_name="user",
    )

    def __str__(self):
        return self.nome
