from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.metStanice, name='metStanice'),
    url(r'^metStanice.json$', views.dajStanice, name='dajStanice'),
]