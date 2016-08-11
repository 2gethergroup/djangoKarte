from django.contrib import admin
from .models import Clanak #import kreiranog modela
    
# Dodavanje kreiranog modela u admin deo
admin.site.register(Clanak) 