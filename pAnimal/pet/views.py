from django.shortcuts import render
from pet.models import Bicho


def index(request):
    return render(request, 'index.html',{})


def bichos(request):
    n = Bicho.objects.all()
    return render(request, 'bichos.html',{'n':n})

def cad_pets(request):
    return render(request, "cad_pets.html", {})

def save_pets(request):
    nd=request.POST['nome_d']
    tel=request.POST['telefone']
    na = request.POST['nome_a']
    ra = request.POST['raca']
    cac = request.POST['caracteristicas']
    pets=Bicho()
    pets.nome_dono=nd
    pets.telefone=tel
    pets.nome_animal=na
    pets.raca=ra
    pets.caracteristicas=cac
    pets.save()
    return render(request, "cad_pets.html", {'msg':"Cadastro Realizado!"})

def edit_pets(request, pk):
    pets=Bicho.objects.get(pk=pk)
    return render(request, "edit_pets.html", {'pets': pets})

def update(request):
    pk=request.POST['pk']
    pets=Bicho.objects.get(pk=pk)
    pets.nome_d=request.POST['nome_dono']
    pets.tel=request.POST['telefone']
    pets.nome_a=request.POST['nome_animal']
    pets.ra=request.POST['raca']
    pets.caracteristicas=request.POST['caracteristicas']
    pets.save()
    return render(request, "edit_pets.html", {'pets': pets})

def deletar_animal(request, pk):
    n = Bicho.objects.get(pk=pk)
    n.delete()
    n = Bicho.objects.all()
    return render(request, 'bichos.html', {'n': n})
