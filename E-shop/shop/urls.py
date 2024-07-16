from django.contrib import admin
from django.urls import path
from store.views import index, product_detail, add_to_cart, cart, delete_cart
from shop import settings
from django.conf.urls.static import static
from accounts.views import signup, logout_user, login_user


#Create les chemins vers les differentes pages
urlpatterns = [
    path('admin/', admin.site.urls), #url admin
    path('signup/', signup, name="signup"), #url page inscription
    path('login/', login_user, name="login"), #url page connexion
    path('logout/', logout_user, name="logout"), #url deconnexion
    path('cart/', cart, name="cart"), #url du panier
    path('cart/delete/', delete_cart, name="delete-cart"), #url pour supprimer du panier
    path('product/<str:slug>/', product_detail, name="product"), #url page d'un produit
    path('product/<str:slug>/add-to-cart/', add_to_cart, name="add-to-cart"), #url pour envoyer dans le panier
    path('', index, name='index'), # url de l'accueil
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
