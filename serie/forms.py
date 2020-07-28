from django import forms

from serie.models import Serie


class SerieForm(forms.ModelForm):

    class Meta:
        model = Serie
        fields = '__all__'