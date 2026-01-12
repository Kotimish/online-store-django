from django.urls import path

from online_store import views

urlpatterns = [
    path('', views.IndexTemplateView.as_view(), name='index'),
    path('about/', views.AboutTemplateView.as_view(), name='about'),
    path('categories/', views.CategoriesListView.as_view(), name='categories_page'),
    path('categories/<int:category_id>/products', views.ProductsListByCategoryView.as_view(), name='products_in_category_page'),
    path('products/', views.ProductsListView.as_view(), name='products_page'),
    path('products/add/', views.ProductCreateView.as_view(), name='post_add'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
]