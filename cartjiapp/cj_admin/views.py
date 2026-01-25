from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from django.contrib import messages

from cartjiapp.models import (
    Category, SubCategory,
    Product, ProductImage,
    Order, Coupon,
    Color, Size
)

from .forms import (
    CJCategoryForm,
    CJSubCategoryForm,
    CJProductCreateForm,
    CJProductImageForm,
    CJColorForm,
    CJSizeForm,
    CJCouponForm,
)

# --------------------------------------------------
# COMMON
# --------------------------------------------------

def cj_admin_only(user):
    return user.is_staff


# --------------------------------------------------
# AUTH
# --------------------------------------------------

def cj_login(request):
    error = None
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
        if user and user.is_staff:
            login(request, user)
            return redirect("cj_dashboard")
        error = "Invalid credentials or not an admin user"

    return render(request, "cj_admin/cj_login.html", {"error": error})


def cj_logout(request):
    logout(request)
    return redirect("cj_login")


# --------------------------------------------------
# DASHBOARD
# --------------------------------------------------

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_dashboard(request):
    context = {
        "total_products": Product.objects.count(),
        "total_orders": Order.objects.count(),
        "total_customers": Order.objects.values("phone").distinct().count(),
        # "total_revenue": Order.objects.aggregate(
        #     total=Sum("price")
        # )["total"] or 0,
        "total_revenue": Order.objects.filter(status="paid")
        .aggregate(total=Sum("price"))["total"] or 0,
    }
    return render(request, "cj_admin/cj_dashboard.html", context)



# --------------------------------------------------
# CATEGORIES
# --------------------------------------------------

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_categories(request):
    return render(
        request,
        "cj_admin/category/cj_categories.html",
        {"categories": Category.objects.all().order_by("name")}
    )


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_category_form(request, pk=None):
    category = Category.objects.filter(pk=pk).first()
    form = CJCategoryForm(request.POST or None, request.FILES or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect("cj_categories")
    return render(request, "cj_admin/category/cj_category_form.html", {"form": form})


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_category_delete(request, pk):
    get_object_or_404(Category, pk=pk).delete()
    return redirect("cj_categories")


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_subcategories(request):
    return render(
        request,
        "cj_admin/subcategory/cj_subcategories.html",
        {"subcategories": SubCategory.objects.select_related("category")}
    )


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_subcategory_form(request, pk=None):
    sub = SubCategory.objects.filter(pk=pk).first()
    form = CJSubCategoryForm(request.POST or None, instance=sub)
    if form.is_valid():
        form.save()
        return redirect("cj_subcategories")
    return render(request, "cj_admin/subcategory/cj_subcategory_form.html", {"form": form})


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_subcategory_delete(request, pk):
    get_object_or_404(SubCategory, pk=pk).delete()
    return redirect("cj_subcategories")






# --------------------------------------------------
# COLORS & SIZES
# --------------------------------------------------

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_colors(request):
    return render(
        request,
        "cj_admin/colorsize/cj_colors.html",
        {"colors": Color.objects.all().order_by("name")}
    )


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_color_form(request, pk=None):
    color = Color.objects.filter(pk=pk).first()
    form = CJColorForm(request.POST or None, instance=color)
    if form.is_valid():
        form.save()
        return redirect("cj_colors")
    return render(request, "cj_admin/colorsize/cj_color_form.html", {"form": form})


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_color_delete(request, pk):
    get_object_or_404(Color, pk=pk).delete()
    return redirect("cj_colors")


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_sizes(request):
    return render(
        request,
        "cj_admin/colorsize/cj_sizes.html",
        {"sizes": Size.objects.all().order_by("name")}
    )


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_size_form(request, pk=None):
    size = Size.objects.filter(pk=pk).first()
    form = CJSizeForm(request.POST or None, instance=size)
    if form.is_valid():
        form.save()
        return redirect("cj_sizes")
    return render(request, "cj_admin/colorsize/cj_size_form.html", {"form": form})


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_size_delete(request, pk):
    get_object_or_404(Size, pk=pk).delete()
    return redirect("cj_sizes")








# --------------------------------------------------
# PRODUCTS
# --------------------------------------------------

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_products(request):
    products = Product.objects.all().order_by("-created_at")
    return render(request, "cj_admin/products/cj_products.html", {"products": products})


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_product_add_edit(request, pk=None):
    product = Product.objects.filter(pk=pk).first()

    ImageFormSet = ProductImageFormSet = ProductImageFormSet = None
    from django.forms import modelformset_factory
    ImageFormSet = modelformset_factory(
        ProductImage,
        form=CJProductImageForm,
        extra=1,
        can_delete=True
    )

    if request.method == "POST":
        product_form = CJProductCreateForm(request.POST, instance=product)
        image_formset = ImageFormSet(
            request.POST,
            request.FILES,
            queryset=ProductImage.objects.filter(product=product)
        )

        if product_form.is_valid() and image_formset.is_valid():
            product = product_form.save()
            product.sizes.set(product_form.cleaned_data["sizes"])

            images = image_formset.save(commit=False)
            for img in images:
                img.product = product
                img.save()

            for img in image_formset.deleted_objects:
                img.delete()

            return redirect("cj_products")

    else:
        product_form = CJProductCreateForm(instance=product)
        image_formset = ImageFormSet(
            queryset=ProductImage.objects.filter(product=product)
        )

    return render(
        request,
        "cj_admin/products/cj_product_form.html",
        {
            "product_form": product_form,
            "image_formset": image_formset,
            "product": product,
            "is_edit": bool(pk),
        }
    )


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted")
        return redirect("cj_products")

    return render(
        request,
        "cj_admin/products/product_delete_confirm.html",
        {"product": product}
    )

# --------------------------------------------------
# ORDERS (NO ADD ORDER)
# --------------------------------------------------

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_orders(request):
    return render(
        request,
        "cj_admin/order/orders_list.html",
        {"orders": Order.objects.all().order_by("-created_at")}
    )


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, "cj_admin/order/order_detail.html", {"order": order})


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_order_edit(request, id):
    order = get_object_or_404(Order, id=id)
    sizes = Size.objects.all()
    colors = Color.objects.all()

    if order.status == "paid":
        messages.error(request, "Paid orders cannot be edited.")
        return redirect("cj_orders")

    if request.method == "POST":

    # 🔒 block editing paid orders
        if order.status == "paid":
            messages.error(request, "Paid orders cannot be edited.")
            return redirect("cj_orders")

        new_status = request.POST.get("status")

        allowed_transitions = {
            "pending": ["confirmed", "cancelled"],
            "confirmed": ["paid", "cancelled"],
            "paid": [],
            "cancelled": [],
        }

        # ❌ invalid status change
        if new_status not in allowed_transitions[order.status]:
            messages.error(
                request,
                f"Invalid status change: {order.status} → {new_status}"
            )
            return redirect("cj_orders")

        # ✅ valid update
        order.customer_name = request.POST.get("customer_name")
        order.phone = request.POST.get("phone")
        order.size = request.POST.get("size") or ""
        order.color = request.POST.get("color") or ""
        order.status = new_status
        order.save()

        return redirect("cj_orders")


    return render(
        request,
        "cj_admin/order/order_edit.html",
        {"order": order, "sizes": sizes, "colors": colors}
    )



# --------------------------------------------------
# COUPONS
# --------------------------------------------------

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_coupons(request):
    return render(
        request,
        "cj_admin/coupons/coupons_list.html",
        {"coupons": Coupon.objects.all().order_by("-id")}
    )


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_coupon_add(request):
    form = CJCouponForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cj_coupons")
    return render(request, "cj_admin/coupons/coupon_form.html", {"form": form})


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_coupon_edit(request, pk):
    coupon = get_object_or_404(Coupon, pk=pk)
    form = CJCouponForm(request.POST or None, instance=coupon)
    if form.is_valid():
        form.save()
        return redirect("cj_coupons")
    return render(request, "cj_admin/coupons/coupon_form.html", {"form": form})


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_coupon_delete(request, pk):
    get_object_or_404(Coupon, pk=pk).delete()
    return redirect("cj_coupons")











# --------------------------------------------------
# AJAX HELPERS
# --------------------------------------------------

from django.http import JsonResponse

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_get_subcategories(request):
    category_id = request.GET.get("category")

    if not category_id:
        return JsonResponse([], safe=False)

    subcategories = SubCategory.objects.filter(category_id=category_id)

    data = [
        {"id": sub.id, "name": sub.name}
        for sub in subcategories
    ]

    return JsonResponse(data, safe=False)
