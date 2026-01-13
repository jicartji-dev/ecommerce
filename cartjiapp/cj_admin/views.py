from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect,render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.db.models import Sum

# import ONLY models you need
from cartjiapp.models import Category, Coupon, Order,  OrderItem, Product, Color, ProductImage, Size, SubCategory
from .forms import (
    CJCategoryForm,
    CJColorForm,
    CJCouponForm,
    CJOrderForm,
    CJOrderItemForm,
    CJProductCreateForm,
    CJSizeForm,
    CJSubCategoryForm,
    CJProductImageForm,
)
from django.shortcuts import get_object_or_404



def cj_admin_only(user):
    return user.is_staff

from django.db.models import Count
from django.db.models import Sum

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_dashboard(request):
    total_products = Product.objects.count()

    # ✅ UNIQUE customers by phone
    unique_customers = (
        Order.objects
        .values("phone")
        .distinct()
        .count()
    )

    total_orders = Order.objects.count()

    total_revenue = Order.objects.aggregate(
        total=Sum("total_amount")
    )["total"] or 0

    context = {
        "total_products": total_products,
        "total_customers": unique_customers,  # 👈 now by phone
        "total_orders": total_orders,
        "total_revenue": total_revenue,
    }

    return render(request, "cj_admin/cj_dashboard.html", context)


def cj_login(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect("cj_dashboard")
        else:
            error = "Invalid credentials or not an admin user"

    return render(request, "cj_admin/cj_login.html", {"error": error})

def cj_logout(request):
    logout(request)
    return redirect("cj_login")



@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_products(request):
    products = Product.objects.all().order_by("-created_at")
    return render(
        request,
        "cj_admin/products/cj_products.html",
        {"products": products}
    )


# begin

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_colors(request):
    colors = Color.objects.all().order_by("name")
    return render(
        request,
        "cj_admin/colorsize/cj_colors.html",
        {"colors": colors}
    )

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_color_form(request, pk=None):
    color = get_object_or_404(Color, pk=pk) if pk else None
    form = CJColorForm(request.POST or None, instance=color)

    if form.is_valid():
        form.save()
        return redirect("cj_colors")

    return render(
        request,
        "cj_admin/colorsize/cj_color_form.html",
        {
            "form": form,
            "title": "Edit Color" if pk else "Add Color"
        }
    )

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_color_delete(request, pk):
    color = get_object_or_404(Color, pk=pk)
    color.delete()
    return redirect("cj_colors")


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_sizes(request):
    sizes = Size.objects.all().order_by("name")
    return render(
        request,
        "cj_admin/colorsize/cj_sizes.html",
        {"sizes": sizes}
    )

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_size_form(request, pk=None):
    size = get_object_or_404(Size, pk=pk) if pk else None
    form = CJSizeForm(request.POST or None, instance=size)

    if form.is_valid():
        form.save()
        return redirect("cj_sizes")

    return render(
        request,
        "cj_admin/colorsize/cj_size_form.html",
        {
            "form": form,
            "title": "Edit Size" if pk else "Add Size"
        }
    )

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_size_delete(request, pk):
    size = get_object_or_404(Size, pk=pk)
    size.delete()
    return redirect("cj_sizes")


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_categories(request):
    categories = Category.objects.all().order_by("name")
    return render(
        request,
        "cj_admin/category/cj_categories.html",
        {"categories": categories}
    )

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_category_form(request, pk=None):
    category = get_object_or_404(Category, pk=pk) if pk else None
    form = CJCategoryForm(request.POST or None, request.FILES or None, instance=category)

    if form.is_valid():
        form.save()
        return redirect("cj_categories")

    return render(
        request,
        "cj_admin/category/cj_category_form.html",
        {
            "form": form,
            "title": "Edit Category" if pk else "Add Category"
        }
    )

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect("cj_categories")


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_subcategories(request):
    subcategories = SubCategory.objects.select_related("category").order_by("category__name", "name")
    return render(
        request,
        "cj_admin/subcategory/cj_subcategories.html",
        {"subcategories": subcategories}
    )


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_subcategory_form(request, pk=None):
    subcategory = get_object_or_404(SubCategory, pk=pk) if pk else None
    form = CJSubCategoryForm(request.POST or None, instance=subcategory)

    if form.is_valid():
        form.save()
        return redirect("cj_subcategories")

    return render(
        request,
        "cj_admin/subcategory/cj_subcategory_form.html",
        {
            "form": form,
            "title": "Edit SubCategory" if pk else "Add SubCategory"
        }
    )


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_subcategory_delete(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    subcategory.delete()
    return redirect("cj_subcategories")


from django.forms import modelformset_factory
from django.db import transaction
from cartjiapp.models import ProductImage



@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_products(request):
    products = Product.objects.all().order_by("-created_at")
    return render(
        request,
        "cj_admin/products/cj_products.html",
        {"products": products}
    )

# @user_passes_test(cj_admin_only, login_url="cj_login")
# def cj_product_add(request):
#     ImageFormSet = modelformset_factory(
#         ProductImage,
#         form=CJProductImageForm,
#         extra=1,          # number of image fields shown
#         can_delete=False
#     )

#     if request.method == "POST":
#         product_form = CJProductCreateForm(request.POST)
#         image_formset = ImageFormSet(request.POST, request.FILES, queryset=ProductImage.objects.none())

#         if product_form.is_valid() and image_formset.is_valid():
#             with transaction.atomic():
#                 # 1️⃣ Save product
#                 product = product_form.save()

#                 # 2️⃣ Save sizes (M2M)
#                 product.sizes.set(product_form.cleaned_data["sizes"])

#                 # 3️⃣ Save images
#                 for form in image_formset:
#                     if form.cleaned_data:
#                         img = form.save(commit=False)
#                         img.product = product
#                         img.save()

#             return redirect("cj_products")

#     else:
#         product_form = CJProductCreateForm(request.POST)
#         image_formset = ImageFormSet(queryset=ProductImage.objects.none())

#     return render(
#         request,
#         "cj_admin/product_add_all.html",
#         {
#             "product_form": product_form,
#             "image_formset": image_formset,
#         }
#     )


from django.forms import modelformset_factory
from django.db import transaction
from cartjiapp.models import Product, ProductImage, Size
from .forms import CJProductCreateForm, CJProductImageForm


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_product_add_edit(request, pk=None):
    product = None
    if pk:
        product = Product.objects.get(pk=pk)

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
            if product else ProductImage.objects.none()
        )

        if product_form.is_valid() and image_formset.is_valid():
            with transaction.atomic():
                # Save product
                product = product_form.save()

                # Save sizes
                product.sizes.set(product_form.cleaned_data["sizes"])

                # Save images
                images = image_formset.save(commit=False)
                for img in images:
                    img.product = product
                    img.save()

                # Delete removed images
                for obj in image_formset.deleted_objects:
                    obj.delete()

            return redirect("cj_products")

    else:
        product_form = CJProductCreateForm(instance=product)
        image_formset = ImageFormSet(
            queryset=ProductImage.objects.filter(product=product)
            if product else ProductImage.objects.none()
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


from django.contrib import messages

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully")
        return redirect("cj_products")

    return render(
        request,
        "cj_admin/products/product_delete_confirm.html",
        {"product": product}
    )

def generate_order_id():
    last_order = Order.objects.order_by("-id").first()

    if last_order and last_order.order_id:
        last_number = int(last_order.order_id.replace("CJ", ""))
        new_number = last_number + 1
    else:
        new_number = 1

    return f"CJ{new_number:05d}"   # CJ00001


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_orders(request):
    orders = Order.objects.all().order_by("-created_at")
    return render(request, "cj_admin/order/orders_list.html", {"orders": orders})

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_order_add(request):

    OrderItemFormSet = modelformset_factory(
        OrderItem,
        form=CJOrderItemForm,
        extra=1,
        can_delete=True
    )

    if request.method == "POST":
        order_form = CJOrderForm(request.POST)
        item_formset = OrderItemFormSet(request.POST, queryset=OrderItem.objects.none())

        if order_form.is_valid() and item_formset.is_valid():
            with transaction.atomic():
                order = order_form.save(commit=False)
                order.order_id = generate_order_id()
                order.total_amount = 0
                order.save()

                total = 0
                for form in item_formset:
                    if form.cleaned_data:
                        item = form.save(commit=False)
                        item.order = order
                        item.save()
                        total += item.price * item.quantity

                order.total_amount = total
                order.save()

            return redirect("cj_orders")

    else:
        order_form = CJOrderForm()
        item_formset = OrderItemFormSet(queryset=OrderItem.objects.none())

    return render(
        request,
        "cj_admin/order/order_add.html",
        {
            "order_form": order_form,
            "item_formset": item_formset,
        }
    )

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(
        request,
        "cj_admin/order/order_detail.html",
        {"order": order}
    )

def cj_order_edit(request, id):
    order = get_object_or_404(Order, id=id)

    if request.method == "POST":
        order.customer_name = request.POST.get("customer_name")
        order.phone = request.POST.get("phone")
        order.address = request.POST.get("address")
        order.status = request.POST.get("status")
        order.save()

        return redirect("cj_orders")

    return render(
        request,
        "cj_admin/order/order_edit.html",
        {"order": order}
    )

def cj_order_delete(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()   # OrderItem auto-deletes (CASCADE)
    return redirect("cj_orders")



@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_coupons(request):
    coupons = Coupon.objects.all().order_by("-id")
    return render(
        request,
        "cj_admin/coupons/coupons_list.html",
        {"coupons": coupons}
    )

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_coupon_add(request):
    form = CJCouponForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("cj_coupons")

    return render(
        request,
        "cj_admin/coupons/coupon_form.html",
        {
            "form": form,
            "title": "Add Coupon"
        }
    )


@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_coupon_edit(request, pk):
    coupon = get_object_or_404(Coupon, pk=pk)
    form = CJCouponForm(request.POST or None, instance=coupon)

    if form.is_valid():
        form.save()
        return redirect("cj_coupons")

    return render(
        request,
        "cj_admin/coupons/coupon_form.html",
        {
            "form": form,
            "title": "Edit Coupon"
        }
    )

@user_passes_test(cj_admin_only, login_url="cj_login")
def cj_coupon_delete(request, pk):
    coupon = get_object_or_404(Coupon, pk=pk)

    if request.method == "POST":
        coupon.delete()
        return redirect("cj_coupons")

    return render(
        request,
        "cj_admin/coupons/coupon_delete.html",
        {"coupon": coupon}
    )

