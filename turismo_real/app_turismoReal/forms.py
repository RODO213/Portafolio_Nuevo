from django import forms
from django.forms import ModelForm

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields =  ['nombreUsuario','password']

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'id': 'registroEmail',
                    'class':'form-control',
                    'placeholder': 'Ingrese su email'
                }
            ),
            
            'password': forms.PasswordInput(
                attrs={
                    'id': 'registroPassword',
                    'class':'form-control',
                    'placeholder': 'Ingrese su contraseña'
                }
            ),
           
        }

    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
        return user
