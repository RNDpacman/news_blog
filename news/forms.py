from django import forms
from .models import News
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from captcha.fields import CaptchaField
from antiblog import settings
import re


class CkeditorAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class ContactForm(forms.Form):
    attrs = {'class': 'form-control'}
    attrs_body = attrs
    attrs_body.update({'rows': 5})

    subject = forms.CharField(
        max_length=150,
        label='Тема',
        widget=forms.TextInput(attrs=attrs),
    )
    body = forms.CharField(
        max_length=2048,
        label='Текст',
        widget=forms.Textarea(attrs=attrs_body)
    )
    captcha = CaptchaField()


class UserLoginForm(AuthenticationForm):
    attrs = {'class': 'form-control'}

    username = forms.CharField(
        max_length=150,
        label='Имя Пользователя',
        widget=forms.TextInput(attrs=attrs),
    )
    password = forms.CharField(
        max_length=500,
        label='Пароль',
        widget=forms.PasswordInput(attrs=attrs)
    )


class UserRegisterForm(UserCreationForm):
    attrs = {'class': 'form-control'}

    username = forms.CharField(
        max_length=150,
        label='Имя Пользователя',
        widget=forms.TextInput(attrs=attrs),
    )
    password1 = forms.CharField(
        max_length=500,
        label='Пароль',
        widget=forms.PasswordInput(attrs=attrs)
    )
    password2 = forms.CharField(
        max_length=500,
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs=attrs)
    )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs=attrs)
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = (
            'title',
            'content',
            'is_published',
            'category',
            'photo',
        )
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
            }),
            'category': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'photo': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }

    def clean_photo(self):
        '''
        Validate file size
        '''
        max_size = settings.MAX_SIZE_UPLOAD_IMAGE
        photo = self.cleaned_data['photo']
        if not photo:
            return
        if photo.size > max_size:
            raise ValidationError('File is too large')
        return photo
