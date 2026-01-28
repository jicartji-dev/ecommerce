from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product


# ✅ Static Pages Sitemap
class StaticSitemap(Sitemap):
    priority = 1.0
    changefreq = "daily"

    def items(self):
        return [
            "home",
            "product_list",
            "about",
            "contact",
            "faq",
            "terms",
            "privacy",
            "store_policy",
        ]

    def location(self, item):
        return reverse(item)


# ✅ Product Pages Sitemap
class ProductSitemap(Sitemap):
    priority = 0.9
    changefreq = "weekly"

    def items(self):
        return Product.objects.filter(is_active=True)
        
