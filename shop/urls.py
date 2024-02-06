from django.urls import path
from .views import ShopHomePageView, ProductListPageView, DetailedProductPageView

urlpatterns = [
    path("shop/", ShopHomePageView.as_view(), name="shop_home_page"),
    path("products/", ProductListPageView.as_view(), name="product_list_page"),
    path("products/<int:product_id>/", DetailedProductPageView.as_view(), name="detailed_product_page"),
]
