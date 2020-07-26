from django import forms

class GeneroForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(GeneroForm, self).__init__(*args, **kwargs)
        self.fields['genero'].error_messages = {'required': 'Campo obrigatório'}

    descricao = forms.CharField(label='Gênero:',required=True)