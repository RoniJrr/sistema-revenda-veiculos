# urls do app veiculos
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # página inicial
    path('listar/', views.listar_veiculos, name='listar_veiculos'),
    path('cadastrar/', views.cadastrar_veiculo, name='cadastrar_veiculo'),
    path('editar/<int:id>/', views.editar_veiculo, name='editar_veiculo'),
    path('excluir/<int:id>/', views.excluir_veiculo, name='excluir_veiculo'),
    path('detalhes/<int:id>/', views.detalhes_veiculo, name='detalhes_veiculo'),
]
