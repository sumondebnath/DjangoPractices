from django import forms
from album.models import Album

class albumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"