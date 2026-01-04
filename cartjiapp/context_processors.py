from .models import Category, SubCategory

def nav_categories(request):
    return {
        "nav_categories": Category.objects.all(),
        
        "nav_subcategories": SubCategory.objects.all(),


    }

