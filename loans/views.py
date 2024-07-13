from django.shortcuts import render

def property(request):
    context={

    }
    return render(request, "loan/app/property.html", context)

def home(request):
    context={

    }
    return render(request, "loan/app/home.html", context)
