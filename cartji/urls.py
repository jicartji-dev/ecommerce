from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cartjiapp.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
