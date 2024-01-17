from musician.models import Musician
from django import forms

class musicianForm(forms.ModelForm):
    class Meta:
        model = Musician
        fields = "__all__"