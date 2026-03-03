# core/forms.py
from allauth.account.forms import LoginForm

class CustomLoginForm(LoginForm):
    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        # Puedes personalizar aquí los widgets
        self.fields['login'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Correo o usuario'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Contraseña'})