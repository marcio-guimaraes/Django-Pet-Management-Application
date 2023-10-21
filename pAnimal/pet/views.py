from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
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
    return redirect('bichos')

#def edit_pets(request, pk):
   # pets=Bicho.objects.get(pk=pk)
   # return render(request, "edit_pets.html", {'pets': pets})

def update(request, pk):
    pet = get_object_or_404(Bicho, pk=pk)

    if request.method == 'POST':
        pet.nome_dono = request.POST.get('nome_dono', pet.nome_dono)
        pet.telefone = request.POST.get('telefone', pet.telefone)
        pet.nome_animal = request.POST.get('nome_animal', pet.nome_animal)
        pet.raca = request.POST.get('raca', pet.raca)
        pet.caracteristicas = request.POST.get('caracteristicas', pet.caracteristicas)
        pet.data = request.POST.get('data', pet.data)

        pet.save()
        return redirect('bichos')  # Redireciona para a lista de animais após a atualização
    else:
        return render(request, "edit_pets.html", {'pets': pet})
def deletar_animal(request, pk):
    animal = get_object_or_404(Bicho, pk=pk)
    animal.delete()
    messages.success(request, 'O animal foi excluído com sucesso.')

    return redirect('bichos')
