from django.shortcuts import render
from django.utils import timezone #modul za vreme
from .models import Clanak # kalasa Clanak

# Create your views here.
def lista_clanaka(request):
	#Ulancani Queri set smesтеn u promenljuvu clanci
	clanci = Clanak.objects.filter(datumObjave__lte=timezone.now()
								).order_by('datumObjave')
	#dodat poslednji parametar {'clanci': clanci}
	return render(request, 'blogDjangoKarte/pocetna.html',  {'clanci': clanci})
