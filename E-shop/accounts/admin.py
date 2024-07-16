from django.contrib import admin
from accounts.models import Shopper

#Ajout de la class des Users sur l'espace Admin
admin.site.register(Shopper)
