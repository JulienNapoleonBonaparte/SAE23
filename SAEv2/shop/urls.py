from django.urls import path
from . import views
from .views import CheckoutView

urlpatterns = [
    path('', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.login_page, name="login"),
    path('logout', views.logout_page, name="logout"),
    path('cart', views.cart_page, name="cart"),
    path('fav', views.fav_page, name="fav"),
    path('favviewpage', views.favviewpage, name="favviewpage"),
    path('remove_fav/<str:fid>', views.remove_fav, name="remove_fav"),
    path('remove_cart/<str:cid>', views.remove_cart, name="remove_cart"),
    path('collections', views.collections, name="collections"),
    path('collections/<str:name>', views.collectionsview, name="collections"),
    path('collections/<str:cname>/<str:pname>', views.product_details, name="product_details"),
    path('addtocart', views.add_to_cart, name="addtocart"),
    path('create_category/', views.create_category, name='create_category'),
    path('create_product/', views.create_product, name='create_product'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]