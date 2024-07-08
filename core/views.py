from django.conf import settings
from django.shortcuts import render, redirect
from django.utils import translation

def index(request):
    context = {}
    return render(request, "core/app/index.html", context)

def set_language(request):
    user_language = request.GET.get('language', 'en')
    translation.activate(user_language)
    response = redirect(request.META.get('HTTP_REFERER'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    print(f"Language activated: {user_language}")  # Debug statement
    return response