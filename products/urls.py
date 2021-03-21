from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-product/', views.addProduct, name='add-product'),
    path('edit-product/<str:pk>', views.editProduct, name='edit-product'),
    path('delete/<str:pk>', views.deleteProduct, name='delete'),
    path('search-product-result', views.ProductSearchResults.as_view(), name='search-product-result'),
    path('cart/', views.cart, name="cart"),
]