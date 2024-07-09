from datetime import datetime
from django.shortcuts import render, redirect

def index(request):
    current_date = datetime.now().strftime("%A, %B %d, %Y")
    context = {
        'current_date': current_date
    }
    return render(request, "core/app/index.html", context)
