from django.db import models
from django.urls import reverse
from shop.settings import AUTH_USER_MODEL
from django.utils import timezone

#Create la class Product 

class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    category = models.CharField(max_length=128)
    price = models.FloatField(default=0.0)
    stock = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products", blank=True, null=True)


#Permet d'afficher le nom et le stock dans le l'espace admin
    def __str__(self):
        return f"{self.name} ({self.stock})"

#Pour gerer l'url des differents products
    def get_absolute_url(self):
        return reverse("product", kwargs={"slug":self.slug})

#Create Article

class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE) #Si on supprime le users, ca supprime les articles
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False) #Commandé ou non
    ordered_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"


#Create Panier
class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)#Autorise un seul panier par user
    orders = models.ManyToManyField(Order) #Articles

    def __str__(self):
        return self.user.username

    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.ordered = True
            order.ordered_date = timezone.now()
            order.save()

        self.orders.clear()
        super().delete(*args, **kwargs)
