from django.db import models
from django.utils import timezone #modul za vreme i datum
# Create your models here.

# Klasa Clanak koja je instanca apstraktne klase Model
class Clanak(models.Model):

	# naslov clanka kao tekstualno polje maksimalne duzine 100 karaktera
	naslov = models.CharField(max_length=100)
	# kratak opis kao tekstualno polje maksimalne duzine 300 karaktera
	kratakOpis = models.CharField(max_length=300)
	# tekst clanka kao tekstualno polje
	tekst = models.TextField()
	# autor clanka kao Django user koji ce biti definisan u narednom poglavlju
	autor = models.ForeignKey('auth.User')
	# datum kreiranja kao polje DateTime 
	datumKreiranja = models.DateTimeField(
			default=timezone.now)
	# datum objave kao polje DateTime
	datumObjave = models.DateTimeField(
			blank=True, null=True)

	# Metoda za objavljivanje clanka
	def objaviClanak(self):
		self.datumObjave = timezone.now()
		self.save()

	# Metoda koja vraca naslov clanka
	def __str__(self):
		return self.naslov