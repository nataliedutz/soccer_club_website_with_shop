from django.shortcuts import render, get_object_or_404
from django.views import View
from django.urls import reverse
from .models import Item

class ShopHomePageView(View):
    def get(self, request):
        return render(request, 'shop.html')

class ProductListPageView(View):
    def get(self, request):
        products = Item.objects.all()  # Fetch all products from the database
        return render(request, 'product_list_page.html', {'products': products})

class DetailedProductPageView(View):
    def get(self, request, product_id):
        # Retrieve the product object based on the provided ID
        product = get_object_or_404(Item, pk=product_id)
        
        # Pass the product object to the template for rendering
        return render(request, 'detailed_product_page.html', {'product': product})

