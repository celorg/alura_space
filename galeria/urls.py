from django.urls import path
from galeria.views import index, imagem, buscar, tag

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('tag/<str:foto_categoria>', tag ,name='tag'),
    path('buscar', buscar, name="buscar"),
    
]