from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product, Cart, Order
from django.urls import reverse

# Create les vues pour recuperer les infos des Products et les envoyer sur les pages

def index(request):
    products = Product.objects.all()
    return render(request, 'store/index.html', context={"products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', context={"product": product} )

def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug) #Verifie si l'article existe
    cart, _ = Cart.objects.get_or_create(user=user) #Create le panier ou recupere le panier
    order, created = Order.objects.get_or_create(user=user, ordered=False, product=product)

    if created: #Si l'article n'existe pas dans le panier
        cart.orders.add(order) #Ajout au panier
        cart.save() #Save le panier
    else: #Si l'article existe deja dans le panier
        order.quantity += 1 #Ajoute un element au panier
        order.save()

    return redirect(reverse("product", kwargs={"slug": slug})) #Redirige vers la page du produit


#Create les vues du Panier

def cart(request):
    cart = get_object_or_404(Cart, user=request.user) #On vérifie si le panier lié a user existe et on renvoi

    return render(request, 'store/cart.html', context={"orders": cart.orders.all()}) #Renvoi vers le panier



#Create les vues pour supprimer du Panier

def delete_cart(request):
    cart = request.user.cart
    if cart:
        cart.delete() #Supprime le panier

    return redirect('index') # Renvoi sur l'index
