from django.shortcuts import render

def aboutmain(request):
    context={

    }
    return render(request, "aboutus/app/aboutmain.html", context)