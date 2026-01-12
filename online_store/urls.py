from django.urls import path
from online_store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories_page, name='categories_page'),
    path('products/', views.products_page, name='products_page'),
    path('categories/<int:category_id>/products', views.products_in_category_page, name='products_in_category_page'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
]