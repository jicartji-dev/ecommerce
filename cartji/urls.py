from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include

from django.contrib.sitemaps.views import sitemap
from cartjiapp.sitemaps import StaticSitemap
sitemaps = {
    "static": StaticSitemap,
}

urlpatterns = [
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path('admin/', admin.site.urls),
    path('', include('cartjiapp.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r"^(?P<path>.*)$", serve),
]
