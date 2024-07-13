from django.shortcuts import render

def aboutmain(request):
    context={

    }
    return render(request, "aboutus/app/aboutmain.html", context)

def financialhealth(request):
    context={

    }
    return render(request, "aboutus/app/financehealth.html", context)


def commitment(request):
    context={

    }
    return render(request, "aboutus/app/commitment.html", context)


def chairman(request):
    context={

    }
    return render(request, "aboutus/app/chairman.html", context)


def directors(request):
    context={

    }
    return render(request, "aboutus/app/directors.html", context)

def bankstaff(request):
    context={

    }
    return render(request, "aboutus/app/bankstaff.html", context)
