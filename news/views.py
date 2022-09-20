from django.shortcuts import get_object_or_404
from django.shortcuts import get_list_or_404
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.messages import constants as message_constants
from .forms import UserRegisterForm, UserLoginForm, ContactForm
from django.core.mail import send_mail
from antiblog import settings


'''
Views основанные на функциях
'''


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            is_success_send = send_mail(
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['body'],
                from_email=settings.FROM_EMAIL,
                recipient_list=settings.RECIPIENT_LIST,
                fail_silently=False,
            )
            if is_success_send:
                messages.success(request, 'Сообщение отправлено')
                return redirect('contact')
            else:
                messages.error(request, 'Проблемы с отправкой')

        else:
            messages.error(request, 'Валидация не прошла')
    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'news/contact.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы зарегистрированы')
            return redirect('news')
        else:
            messages.error(request, 'Ошибка регистрации')

    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'news/register.html', context=context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Вы вошли как {user.get_username()}')
            return redirect('news')
        else:
            messages.error(request, 'Ошибка аутентификации')

    else:
        form = UserLoginForm()
    context = {'form': form}

    return render(request, 'news/login.html', context=context)

def user_logout(request):
    logout(request)
    messages.success(request, 'Вы вышли')
    return redirect('news')





