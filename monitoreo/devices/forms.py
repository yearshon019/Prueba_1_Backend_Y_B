from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Organization  # Importa desde la misma app

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned = super().clean()
        email = cleaned.get("email")
        password = cleaned.get("password")
        try:
            user = User.objects.get(email=email)
            auth_user = authenticate(username=user.username, password=password)
            if not auth_user:
                raise forms.ValidationError("Credenciales inválidas.")
            cleaned["user"] = auth_user
        except User.DoesNotExist:
            raise forms.ValidationError("Credenciales inválidas.")
        return cleaned


class RegisterForm(forms.Form):
    org_name = forms.CharField(label="Company name", max_length=100)
    org_rut = forms.CharField(label="RUT", max_length=12)
    org_address = forms.CharField(label="Address", max_length=200)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con ese email.")
        return email

    def save(self):
        # Crear Organization y User simple (username = email)
        org = Organization.objects.create(
            name=self.cleaned_data["org_name"],
            rut=self.cleaned_data["org_rut"],
            address=self.cleaned_data["org_address"],
        )
        user = User.objects.create_user(
            username=self.cleaned_data["email"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password"],
        )
        return user, org


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField()
