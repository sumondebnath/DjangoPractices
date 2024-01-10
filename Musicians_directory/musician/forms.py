from django import forms
from musician.models import Musicians

class musiciansForm(forms.ModelForm):
    class Meta:
        model = Musicians
        fields = "__all__"

        labels={
            "ph_no" : "Phone Number",
            "first_name":"First Name",
        }
        widgets ={
            "first_name" : forms.TextInput(attrs={"placeholder":"Enter Your First Name"}),
            "last_name" : forms.TextInput(attrs={"placeholder":"Enter Your Last Name"}),
            "email": forms.EmailInput(attrs={"placeholder":"Enter Your Email Address"}),
            "ph_no" : forms.TextInput(attrs={"placeholder":"Enter Your Phone Number"}),
            "instrument_type":forms.TextInput(attrs={"placeholder": "Enter Your Instruments"}),
        }