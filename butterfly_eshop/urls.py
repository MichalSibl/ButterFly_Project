"""butterfly_eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import stat
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from shop.views import hello_world_view, add_to_cart_view, \
    cart_view, remove_from_cart_view, checkout, HomepageView, ListProductReviewView, \
    DeleteProductReviewView, HelpdeskContactView, ProductReviewUpdateView, \
    LoginView, LogoutView, RegistrationView
from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls.static import static
from django.conf import settings
from shop.views import api_search_view

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello/<str:name>/", hello_world_view, name="hello_world"),
    path("", HomepageView.as_view(), name="homepage"),
    path("add_to_cart/<int:item_pk>/", add_to_cart_view, name="add_to_cart"),
    path("cart/<int:pk>/", cart_view, name="cart_detail"),
    path("checkout/<int:pk>/", checkout, name="checkout"),
    path("remove_from_cart/<int:item_pk>/", remove_from_cart_view, name="remove_from_cart"),
    path("product_review/<int:product_pk>/", ListProductReviewView.as_view(), name="list_product_review"),
    path("delete/product_review/<int:pk>/", DeleteProductReviewView.as_view(), name="delete_product_review"),
    path("add/contact/", HelpdeskContactView.as_view(), name="helpdesk_contact"),
    path("update/product_review/<int:pk>/", ProductReviewUpdateView.as_view(), name="update_product_review"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegistrationView.as_view(), name="register"),
    path("api/search", api_search_view, name="search"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

path("api/search", api_search_view, name="search"),


