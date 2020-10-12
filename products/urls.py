from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.all_products_view, name='all_products'),
    path('shop/<slug>/', views.single_product_view, name='single_product'),
]

