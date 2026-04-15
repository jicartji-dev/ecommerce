from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Coupon, Product, Review, SubCategory
from django.http import HttpResponse
from django.contrib import messages



def home(request):
    categories = Category.objects.all()
    products = Product.objects.filter(is_active=True).order_by('-created_at')[:8]
    reviews = Review.objects.filter(is_active=True).order_by("-created_at")[:8]
    return render(request, 'cartjiapp/index.html', {'products': products, "reviews": reviews,"categories":categories})



def product_list(request):
    sort = request.GET.get("sort")
    products = Product.objects.filter(is_active=True)

    if sort == "new":
        products = products.order_by("-created_at")

    elif sort == "trending":
        products = products.order_by("-views", "-created_at")

    else:
        products = products.order_by("-created_at")

    return render(request, "cartjiapp/product_list.html", {
        "products": products
    })



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)

    # 🔥 increment views
    product.views += 1
    product.save(update_fields=["views"])

    return render(request, 'cartjiapp/product_detail.html', {'product': product})


# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug, is_active=True)
#     return render(request, 'cartjiapp/product_detail.html', {'product': product})

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_active=True).order_by('-created_at')
    return render(request, 'cartjiapp/product_list.html', {
        'category': category,
        'products': products
    })

def subcategory_products(request, category_slug, sub_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(SubCategory, slug=sub_slug, category=category)
    products = Product.objects.filter(
        category=category,
        subcategory=subcategory,
        is_active=True
    ).order_by('-created_at')
    return render(request, 'cartjiapp/product_list.html', {
        'category': category,
        'subcategory': subcategory,
        'products': products
    })

def load_subcategories(request):
    category_id = request.GET.get('category')
    data = list(
        SubCategory.objects.filter(category_id=category_id)
        .values('id', 'name')
    )
    return JsonResponse(data, safe=False)


def about(request):
    return render(request, 'cartjiapp/about.html')

def contact(request):
    return render(request, 'cartjiapp/contact.html')

def shipping_policy(request):
    return render(request, "cartjiapp/shipping.html")

def returns_policy(request):
    return render(request, "cartjiapp/returns.html")

def faq_page(request):
    return render(request, "cartjiapp/faq.html")

def store_policy(request):
    return render(request, "cartjiapp/store_policy.html")

def terms(request):
    return render(request, "cartjiapp/terms.html")


def privacy(request):
    return render(request, "cartjiapp/privacy.html")

def check_coupon(request):
    code = request.GET.get('code')

    try:
        coupon = Coupon.objects.get(code__iexact=code, is_active=True)
        return JsonResponse({
            "valid": True,
            "discount": coupon.discount_percent
        })
    except Coupon.DoesNotExist:
        return JsonResponse({
            "valid": False
        })


def career_part_time(request):
    return render(request, 'cartjiapp/career_part_time.html')


def career_full_time(request):
    return render(request, 'cartjiapp/career_full_time.html')

from django.shortcuts import redirect
from urllib.parse import quote
from .models import Order
from .utils import generate_order_id




def buy_on_whatsapp(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)

    size = request.POST.get("size")
    color = request.POST.get("color")
    final_price = request.POST.get("final_price") or product.selling_price
    coupon_code = request.POST.get("coupon_code", "").strip()

    # full product link
    product_url = request.build_absolute_uri(product.get_absolute_url())

    order = Order.objects.create(
        order_id=generate_order_id(),
        product=product,
        price=final_price,
        size=size,
        color=color,
        payment_method="whatsapp",
        status="pending",
    )

    # 🔹 BASE MESSAGE (always)
    message = f"""
Hi CartJi 👋
I want to order:

Product: {product.name}
Size: {size}
Color: {color}
"""

    # 🔹 ADD DISCOUNT INFO ONLY IF COUPON USED
    if coupon_code and product.original_price and float(final_price) < float(product.original_price):
        discount_amount = float(product.selling_price) - float(final_price)
        message += f"""
Selling Price: ₹{product.selling_price}
Discount Applied: ₹{int(discount_amount)}
Coupon Code: {coupon_code}
"""

    # 🔹 FINAL PRICE + LINK (always)
    message += f"""
Final Price: ₹{final_price}

Product Link:
{product_url}

Order ID: {order.order_id}

Please guide me further.
"""

    whatsapp_url = (
        "https://wa.me/918303278845"
        f"?text={quote(message)}"
    )

    return redirect(whatsapp_url)

def checkout(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)

    # 🔥 get from URL
    size = request.GET.get("size")
    color = request.GET.get("color")


    if not size or not color:
        messages.error(request, "Please select size and color before proceeding to checkout.")
        return redirect("product_detail", slug=slug)

    if request.method == "POST":

        phone = request.POST.get("phone")

        # 🔥 VALIDATION
        if not phone.isdigit() or len(phone) != 10:
            messages.error(request, "Phone number must be exactly 10 digits")
            return redirect(request.path)

        order = Order.objects.create(
            order_id=generate_order_id(),
            product=product,
            price=request.POST.get("final_price") or product.selling_price,
            size=request.POST.get("size"),
            color=request.POST.get("color"),
            customer_name=request.POST.get("name"),
            phone=phone,
            delivery_address=request.POST.get("address"),
            payment_method="online",
            payment_screenshot=request.FILES.get("payment_screenshot"),
            UTR=request.POST.get("utr"),
            status="pending"
        )
        
        from urllib.parse import quote

        # 🔥 UPI DETAILS
        upi_id = "chauhanadarsh432-3@okicici"   # ⚠️ replace with your real UPI ID
        name = "CartJi"

        amount = request.POST.get("final_price") or product.selling_price

        upi_link = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR"

        # 🔥 detect mobile (simple way)
        user_agent = request.META.get("HTTP_USER_AGENT", "").lower()

        if "android" in user_agent or "iphone" in user_agent:
            return redirect(upi_link)   # 📱 direct open UPI app
        else:
            return render(request, "cartjiapp/order_success.html", {
                "order": order,
                "upi_link": upi_link   # 💻 show button manually
            })



    return render(request, "cartjiapp/checkout.html", {
        "product": product,
        "size": size,
        "color": color
    })




def health(request):
    return HttpResponse("OK")



