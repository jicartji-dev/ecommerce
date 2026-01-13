from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Coupon, Product, Review, SubCategory
from django.http import HttpResponse


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



def health(request):
    return HttpResponse("OK")



