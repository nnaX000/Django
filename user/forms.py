from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)  # 이메일 필수

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'id', 'phone_number', 'password1', 'password2']


class LoginForm(forms.Form):
    id = forms.CharField(label='아이디')
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput)

class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'phone_number', 'email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'id' in self.fields:
            self.fields['id'].disabled = True

class CustomPasswordChangeForm(forms.Form):
    pass