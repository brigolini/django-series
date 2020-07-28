from django.shortcuts import render

from . import forms
from . import models


def cadastro(request):
    print("insert")
    print(request.method);
    form = forms.GeneroForm()
    if request.method == 'POST':
        form = forms.GeneroForm(request.POST)
        if form.is_valid():
            print("Saving")
            form.save(commit=True)
        else:
            print("ERROR")
    generos_list = models.Genero.objects.order_by('descricao')
    data_dict = {"genero_records": generos_list, 'form': form}

    return render(request, 'genero/genero.html', data_dict)


def delete(request, id):
    print("delete")
    models.Genero.objects.filter(id=id).delete()
    form = forms.GeneroForm()
    generos_list = models.Genero.objects.order_by('descricao')
    data_dict = {"genero_records": generos_list, 'form': form}
    return render(request, 'genero/genero.html', data_dict)


def update(request, id):
    item = models.Genero.objects.get(id=id);
    if request.method == "GET":
        form = forms.GeneroForm(initial={'descricao': item.descricao})
        data_dict = {'form': form}
        return render(request, 'genero/genero_upd.html', data_dict)
    else:
        form = forms.GeneroForm(request.POST)
        item.descricao = form.data['descricao']
        item.save()
        generos_list = models.Genero.objects.order_by('descricao')
        data_dict = {"genero_records": generos_list, 'form': form}
        return render(request, 'genero/genero.html', data_dict)
