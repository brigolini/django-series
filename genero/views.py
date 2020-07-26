from django.shortcuts import render
from . import forms
# Create your views here.

def cadastro(request):
   form = forms.GeneroForm(request.POST)

   if request.method == 'POST':
      if form.is_valid():
         print("Validado com sucesso")
         print(form.cleaned_data['genero'])

   return render(request,'genero/genero.html',{'form':form})