from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

#ESTO TAMPOCO LE TOMES ATENCION YA QUE ES PARTE DEL LOGUE Y REGISTRO DE LA PAGINA

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Nombre de Usuario',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu Nombre de Usuario'})
    )
    
    first_name = forms.CharField(
        label='Nombre',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu Nombre'})
    )
    
    last_name = forms.CharField(
        label='Apellido',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu Apellido'})
    )
    
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu Email'})
    )
    
    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa tu Contraseña'})
    )
    
    password2 = forms.CharField(
        label='Confirmar Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese Nuevamente su Contraseña'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2'] 

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no Coinciden')
        if len(password1) < 8:
            raise forms.ValidationError('La contraseña debe tener al menos 8 caracteres.')
        return password1
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError('El Nombre de Usuario debe tener al menos 3 caracteres.')
        return username
