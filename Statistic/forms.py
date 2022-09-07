from django import forms
from .models import *
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField


class UserRegistration(UserCreationForm): #forms.ModelForm
    username = forms.CharField(label='Логин:', widget=forms.TextInput())
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Подтвердите пароль:',
                                widget=forms.PasswordInput())
    email = forms.EmailField(label='Почта:', widget=forms.EmailInput())
    captcha = CaptchaField(label='Введите символы с картинки')

    class Meta:
        model = User #Player
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 4:
            raise ValidationError('имя пользователья не должно быть кароче 4 букв')
        return username

