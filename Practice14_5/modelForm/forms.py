from django import forms
from modelForm.models import allFields

class allForms(forms.ModelForm):
    class Meta:
        model = allFields
        fields = "__all__"
        widgets = {
            "date" : forms.DateInput(attrs={"type":"date"}),
            "datetime" : forms.DateTimeInput(attrs={"type":"datetime-local"}),
            "time" : forms.TimeInput(attrs={"type":"time"}),
            "url" : forms.URLInput(),
        }