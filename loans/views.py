from django.shortcuts import render

def property(request):
    return render(request, "loan/app/property.html")

def home(request):
    return render(request, "loan/app/home.html")

def emi_tool(request):
    return render(request, "loan/app/emi_tool.html")

def fd_tool(request):
    return render(request, "loan/app/fd_tool.html")
