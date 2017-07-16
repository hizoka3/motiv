# -*- coding: utf-8 -*-
import requests
import smtplib
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from social_django.models import UserSocialAuth

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'index.html')

@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'core/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'core/password.html', {'form': form})

def spikeGmail(request):
    """
    :param request:
    :return:
    """
    # Data de form

    fromaddr = 'lfuentesl@gmail.com'
    toaddrs = 'rodrigo@thedogcompany.cl'

    # Que mensaje estamos enviando

    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = fromaddr
    msg['To'] = toaddrs

    # Cuerpo del mensaje
    text = "Hola!\n¿Cómo estás?\nTenemos una oferta para ti:\nhttps://blooming-hamlet-35774.herokuapp.com/candidato/postulacion/19/2/"
    html = """\
    <html>
      <head></head>
      <body>
        <p>Hola!<br>
           ¿Cómo estás?<br>
           Tenemos una oferta para ti: <a href="https://blooming-hamlet-35774.herokuapp.com/candidato/postulacion/19/2/">Ver la oferta</a>.
        </p>
      </body>
    </html>
    """

    # Graba los dos tipos MIME
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Hace el attach de las dos partes
    # Sigue la norma RFC 2046,
    # Toma el mensaje HTML por defecto
    msg.attach(part1)
    msg.attach(part2)

    # Gmail Login

    username = 'lfuentesl@gmail.com'
    password = 'Agatha2020+'

    # Enviando mail

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()




#Dashboard
def dashboard(request):
    """
    Funcion para mostrar la plantilla del dashboard        
    :param request:
    :return: httpResponse
    """
    return render(request, 'core/dashboard.html')


def dashboard_ejecutivo(request):
    return render(request, 'core/dashboard_ejecutivo.html')


def dashboard_ejecutivo_single(request):
    return render(request, 'core/dashboard_ejecutivo_single.html')

