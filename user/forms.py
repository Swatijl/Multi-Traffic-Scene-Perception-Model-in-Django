from django import forms

from user.models import RegisterModel, Upload_Model


class RegisterForms(forms.ModelForm):
    class Meta:
        model=RegisterModel
        fields=("firstname","lastname","userid","password","email","gender","mblenum",)

class UploadForm(forms.ModelForm):
    class Meta:
        model=Upload_Model
        fields=("wheather","area","images","state","distric",)
