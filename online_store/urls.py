from django.urls import path
from online_store import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('categories/', views.categories_page, name='categories_page'),
    path('categories/<int:category_id>/products', views.products_in_category_page, name='products_in_category_page'),
    path('products/', views.products_page, name='products_page'),
    path('products/add/', views.product_add_page, name='post_add'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('products/<int:product_id>/edit/', views.product_edit_page, name='product_edit'),
    path('products/<int:product_id>/delete/', views.product_delete_page, name='product_delete'),
]