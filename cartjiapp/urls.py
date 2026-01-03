from django.urls import path
from .views import about,category_products, contact, health, home, load_subcategories, product_detail, product_list, subcategory_products

urlpatterns = [
    path('', home, name='home'),
     path('products/', product_list, name='product_list'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('admin/load-subcategories/', load_subcategories, name='admin_load_subcategories'),
    path('category/<slug:slug>/', category_products, name='category_products'),
    path(
        'category/<slug:category_slug>/<slug:sub_slug>/',
        subcategory_products,
        name='subcategory_products'
    ),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path("health/", health),


]
