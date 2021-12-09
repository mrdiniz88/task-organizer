from django.contrib.auth.forms import UserCreationForm
from django import forms 

from .models import User


class UserSignupForm(UserCreationForm):
    password1 = forms.CharField(
        label='Senha',
        strip=False,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Senha',
                'class': 'form-control'
            }
        )
    )
    
    password2 = forms.CharField(
        label='Confirmar Senha',
        strip=False,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repita a senha',
                'class': 'form-control'
            }
        )
    )
    
    class Meta:
        model = User
        fields = ['username']
        labels = {
            'username': 'Usuário'
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Usuario',
                'class': 'form-control',
            })
        }
        
        
class UserSigninForm(forms.Form):
    username = forms.CharField(
        label = 'Usuário',
        max_length=150,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Usuario',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label = 'Senha',
        strip=False,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Senha',
                'class': 'form-control'
            }
        )
    )