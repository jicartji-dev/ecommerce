from .models import Category, SubCategory

def nav_categories(request):
    return {
        "nav_categories": Category.objects.prefetch_related("subcategories"),        
        "nav_subcategories": SubCategory.objects.all(),


    }

