from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = ["nombre", "correo", "tipo_registro", "mensaje", "avisos"]

        #fields = '__all__'