from django.urls import path
from .views import about,category_products, contact, faq_page, health, home, load_subcategories, privacy, product_detail, product_list, returns_policy, shipping_policy, store_policy, subcategory_products, terms
from django.conf import settings
from django.conf.urls.static import static

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
    path("shipping/", shipping_policy, name="shipping"),
    path("returns/", returns_policy, name="returns"),
    path("faq/", faq_page, name="faq"),
    path("terms/", terms, name="terms"),
    path("privacy/", privacy, name="privacy"),
    path("store-policy/", store_policy, name="store_policy"),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
