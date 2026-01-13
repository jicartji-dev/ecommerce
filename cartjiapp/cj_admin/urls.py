from django.urls import path
from .views import (
    cj_categories,
    cj_category_delete,
    cj_category_form,
    cj_color_delete,
    cj_color_form,
    cj_colors,
    cj_coupon_add,
    cj_coupon_delete,
    cj_coupon_edit,
    cj_coupons,
    cj_dashboard,
    cj_login,
    cj_logout,
    cj_order_add,
    cj_order_delete,
    cj_order_detail,
    cj_order_edit,
    cj_orders,
    # cj_product_add,
    cj_product_add_edit,
    cj_product_delete,
    cj_products,
    cj_size_delete,
    cj_size_form,
    cj_sizes,
    cj_subcategories,
    cj_subcategory_delete,
    cj_subcategory_form,
)

urlpatterns = [

    # begin

    # colors
    path("colors/", cj_colors, name="cj_colors"),
    path("colors/add/", cj_color_form, name="cj_color_add"),
    path("colors/edit/<int:pk>/", cj_color_form, name="cj_color_edit"),
    path("colors/delete/<int:pk>/", cj_color_delete, name="cj_color_delete"),

    # sizes
    path("sizes/", cj_sizes, name="cj_sizes"),
    path("sizes/add/", cj_size_form, name="cj_size_add"),
    path("sizes/edit/<int:pk>/", cj_size_form, name="cj_size_edit"),
    path("sizes/delete/<int:pk>/", cj_size_delete, name="cj_size_delete"),

    # category
    path("categories/", cj_categories, name="cj_categories"),
    path("categories/add/", cj_category_form, name="cj_category_add"),
    path("categories/edit/<int:pk>/", cj_category_form, name="cj_category_edit"),
    path("categories/delete/<int:pk>/", cj_category_delete, name="cj_category_delete"),

    # subcategory
    path("subcategories/", cj_subcategories, name="cj_subcategories"),
    path("subcategories/add/", cj_subcategory_form, name="cj_subcategory_add"),
    path("subcategories/edit/<int:pk>/", cj_subcategory_form, name="cj_subcategory_edit"),
    path("subcategories/delete/<int:pk>/", cj_subcategory_delete, name="cj_subcategory_delete"),
    
    

    # end
    path("login/", cj_login, name="cj_login"),
    path("logout/", cj_logout, name="cj_logout"),


    path("", cj_dashboard, name="cj_dashboard"),

    # product
    path("products/",cj_products,name="cj_products"),
    
    path("products/add/", cj_product_add_edit, name="cj_product_add"),
    path("products/edit/<int:pk>/", cj_product_add_edit, name="cj_product_edit"),
    path("products/delete/<int:pk>/", cj_product_delete, name="cj_product_delete"),


    path("orders/", cj_orders, name="cj_orders"),
    path("orders/add/", cj_order_add, name="cj_order_add"),
    path("orders/<int:pk>/", cj_order_detail, name="cj_order_detail"),
    path("orders/edit/<int:id>/", cj_order_edit, name="cj_order_edit"),
    path("orders/delete/<int:id>/", cj_order_delete, name="cj_order_delete"),


    path("coupons/", cj_coupons, name="cj_coupons"),
    path("coupons/add/", cj_coupon_add, name="cj_coupon_add"),
    path("coupons/edit/<int:pk>/", cj_coupon_edit, name="cj_coupon_edit"),
    path("coupons/delete/<int:pk>/", cj_coupon_delete, name="cj_coupon_delete"),

]
