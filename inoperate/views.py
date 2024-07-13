from django.shortcuts import render, redirect
from inoperate.forms import SearchForm
from inoperate.models import Person
from django.db.models import Sum

from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import logout

User=settings.AUTH_USER_MODEL

def inoperate(request):
    no_of_account = Person.objects.all().count()
    total_amount = Person.objects.aggregate(Sum('amount'))['amount__sum']
    results = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            account_number = form.cleaned_data['account_number']
            results = Person.objects.filter(account_number=account_number)
    else:
        form = SearchForm()
    context={
        'form': form, 
        'results': results,
        'no_of_account':no_of_account,
        'total_amount':total_amount,
    }
    return render(request, "inoperate/app/inoperate.html", context)

def view_full_deaf(request):
    pass

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request,f"Hey, You are already Logged in")
        return redirect('inoperate:view_full_deaf')
    else:
        if request.method=="POST":
            email=request.POST.get("email")
            password=request.POST.get("password")

            try:
                user=User.object.get(email=email)
            except:
                messages.warning(request,f"User with {email} does not exist")

            user=authenticate(request,email=email,password=password)

            if user is not None:
                login(request,user)
                messages.success(request,"Your are logged in.")
                return redirect("inoperate:view_full_deaf")
            
            else:
                messages.warning(request,"User Does not exist, create an accounnt")
    return render(request,"inoperate/app/sign-in.html")


def logout_view(request):
    logout(request)
    messages.success(request, "You Logged-Out, successfully")
    return redirect("inoperate:inoperate")