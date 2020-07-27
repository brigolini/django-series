from django.shortcuts import render

from . import forms
from . import models
# Create your views here.

def cadastro(request):

   form = forms.GeneroForm(request.POST)
   if request.method == 'POST':
      if form.is_valid():
         form.save(commit=True)
      else:
         print("ERROR")
#   if request.method == 'POST':
#      if form.is_valid():
#         print("Validado com sucesso")
#         print(form.cleaned_data['descricao'])
   generos_list = models.Genero.objects.order_by('descricao')
   date_dict = {"genero_records": generos_list,'form':form}

   return render(request,'genero/genero.html',date_dict)