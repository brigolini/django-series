from django.shortcuts import render

from . import forms
from . import models


def cadastro(request):
   if (request.method=='DELETE'):
      print("DELETIZOU")
   form = forms.GeneroForm()
   if request.method == 'POST':
      form = forms.GeneroForm(request.POST)
      if form.is_valid():
         form.save(commit=True)
      else:
         print("ERROR")
   generos_list = models.Genero.objects.order_by('descricao')
   date_dict = {"genero_records": generos_list,'form':form}

   return render(request,'genero/genero.html',date_dict)

def delete(request,id):
   models.Genero.objects.filter(id=id).delete()
   return render(request,'genero/genero.html')
