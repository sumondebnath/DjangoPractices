from django import forms
from album.models import Albums

class albumForm(forms.ModelForm):
    class Meta:
        model = Albums
        fields = "__all__"

        # ratingChoices = {("one", "1"), ("two", "2"), ("three", "3"), ("four", "4"), ("five", "5")}
        # widgets ={
        #     "rating": forms.ChoiceField(choices = ratingChoices)
        # }