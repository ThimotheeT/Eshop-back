from django.contrib import admin
from store.models import Product, Order, Cart

#Ajout de la class Product dans l'espace admin
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Cart)
