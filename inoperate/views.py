from django.shortcuts import render
from inoperate.forms import SearchForm
from inoperate.models import Person
from django.db.models import Sum

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
