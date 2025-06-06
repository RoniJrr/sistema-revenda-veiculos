# Views do CRUD aqui
from django.shortcuts import render, redirect, get_object_or_404
from .models import Veiculo
from .forms import VeiculoForm
from django.urls import reverse
from django.contrib import messages

from django.shortcuts import render
from .models import Veiculo

def home(request):
    veiculos = Veiculo.objects.all()

    # Filtros
    marca = request.GET.get('marca')
    modelo = request.GET.get('modelo')
    ano = request.GET.get('ano')

    if marca:
        veiculos = veiculos.filter(marca__icontains=marca)
    if modelo:
        veiculos = veiculos.filter(modelo__icontains=modelo)
    if ano:
        veiculos = veiculos.filter(ano=ano)

    context = {
        'veiculos': veiculos,
        'filtros': {
            'marca': marca or '',
            'modelo': modelo or '',
            'ano': ano or '',
        }
    }
    return render(request, 'veiculos/home.html', context)


def listar_veiculos(request):
    veiculos = Veiculo.objects.all().order_by('-data_cadastro')

    marca = request.GET.get('marca')
    modelo = request.GET.get('modelo')
    ano = request.GET.get('ano')

    if marca:
        veiculos = veiculos.filter(marca__icontains=marca)
    if modelo:
        veiculos = veiculos.filter(modelo__icontains=modelo)
    if ano:
        veiculos = veiculos.filter(ano=ano)

    return render(request, 'veiculos/listar.html', {'veiculos': veiculos})



def cadastrar_veiculo(request):
    if request.method == 'POST':
        destaque = 'destaque' in request.POST  # checkbox manual
        marca = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        ano = request.POST.get('ano')
        cor = request.POST.get('cor')
        quilometragem = request.POST.get('quilometragem')
        preco = request.POST.get('preco')
        fipe = request.POST.get('fipe')
        foto = request.FILES.get('foto')

        Veiculo.objects.create(
            marca=marca,
            modelo=modelo,
            ano=ano,
            cor=cor,
            quilometragem=quilometragem,
            preco=preco,
            fipe=fipe,
            foto=foto,
            destaque=destaque
        )

        messages.success(request, 'Veículo cadastrado com sucesso!')
        return redirect('listar_veiculos')

    return render(request, 'veiculos/formulario.html', {
        'form': None,
        'titulo': 'Cadastrar Veículo',
        'veiculo': None
    })



def editar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)

    if request.method == 'POST':
        veiculo.marca = request.POST.get('marca')
        veiculo.modelo = request.POST.get('modelo')
        veiculo.ano = request.POST.get('ano')
        veiculo.cor = request.POST.get('cor')
        veiculo.quilometragem = request.POST.get('quilometragem')
        veiculo.preco = request.POST.get('preco')
        veiculo.fipe = request.POST.get('fipe')
        veiculo.destaque = 'destaque' in request.POST  # checkbox
        if request.FILES.get('foto'):
            veiculo.foto = request.FILES.get('foto')
        veiculo.save()
        messages.success(request, 'Veículo atualizado com sucesso!')
        return redirect('listar_veiculos')

    return render(request, 'veiculos/formulario.html', {
        'form': None,
        'titulo': 'Editar Veículo',
        'veiculo': veiculo
    })




def excluir_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    veiculo.delete()
    messages.success(request, 'Veículo excluído com sucesso!')
    return redirect('listar_veiculos')

def detalhes_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    return render(request, 'veiculos/detalhes.html', {'veiculo': veiculo})


