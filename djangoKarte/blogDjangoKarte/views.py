from django.shortcuts import render

# Create your views here.
def lista_clanaka(request):
    return render(request, 'blogDjangoKarte/pocetna.html', {})

