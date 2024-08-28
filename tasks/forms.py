#MDOELO DE FORMULARIO PERSONALIZADO
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserRole

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    role = forms.ModelChoiceField(queryset=UserRole.objects.all(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.role = self.cleaned_data['role']

        # Establecer la contraseña usando set_password para asegurarla
        user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.save()
        return user


#MDOELO DE FORMULARIO PERSONALIZADO FIN
