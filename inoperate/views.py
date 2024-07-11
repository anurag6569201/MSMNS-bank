from django.shortcuts import render
from inoperate.forms import SearchForm
from inoperate.models import Person

def inoperate(request):
    results = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            account_number = form.cleaned_data['account_number']
            results = Person.objects.filter(name=name, account_number=account_number)
    else:
        form = SearchForm()
    context={
        'form': form, 
        'results': results,
    }
    return render(request, "inoperate/app/inoperate.html", context)
