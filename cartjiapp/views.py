from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, SubCategory



def home(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'cartjiapp/index.html', {'products': products})

def product_list(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'cartjiapp/product_list.html', {
        'products': products
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'cartjiapp/product_detail.html', {'product': product})

def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, is_active=True)
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
    )
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
