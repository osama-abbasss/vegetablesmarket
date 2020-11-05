from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_view, name='cart'),
    path('add_to_cart/<slug>/', views.add_item_to_cart, name='add_to_cart'),
    path('remove_multi_items/<slug>/', views.delete_multi_products, name='remove_multi_items'),
    path('remove_single_item/<slug>/', views.delete_single_product, name='remove_single_item'),



]