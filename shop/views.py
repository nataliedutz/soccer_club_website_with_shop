from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from django.urls import reverse
from .models import Order, Item
from .forms import OrderForm
from accounts.models import Profile
from django.contrib.auth.models import User

class ShopHomePageView(View):
    def get(self, request):
        return render(request, 'shop.html')

class ProductListPageView(View):
    def get(self, request):
        products = Item.objects.all()  # Fetch all products from the database
        return render(request, 'product_list_page.html', {'products': products})

class DetailedProductPageView(View):
    def get(self, request, product_id):
        product = get_object_or_404(Item, pk=product_id)
        form = OrderForm(initial={'item': product})
        return render(request, 'detailed_product_page.html', {'product': product, 'form': form})
    
    def post(self, request, product_id):
        if not request.user.is_authenticated:
            return redirect('login') 
        
        print("Post request received")

        product = get_object_or_404(Item, pk=product_id)
        profile = request.user.profile

        # # Check if the user is logged in
        # if not request.user.is_authenticated:
        #     # If not logged in, display a message and redirect to the login page
        #     messages.warning(request, 'Please log in to be able to make an order.')
        #     return redirect('login')

        if request.method == 'POST':
            print("POST method detected")

            form = OrderForm(request.POST)
            if form.is_valid():
                print("Form is valid")
                order = form.save(commit=False)
                order.item = product
                order.profile = profile 
                order.save()
                print("Order saved successfully")

            # Update item quantity or delete item
            quantity = form.cleaned_data.get('quantity', 1)
            product.quantity -= quantity
            if product.quantity <= 0:
                try:
                    product.delete()
                except Exception as e:
                    print(f"Error deleting product: {e}")

            else:
                product.save()

            # Redirect to order success view
            return redirect('order_success') 
        else:
            form = OrderForm(initial={'item': product}) 
        # Form is not valid, re-render the page with the form and product
            return render(request, 'detailed_product_page.html', {'product': product, 'form': form})
        
@login_required
def order_success_view(request):
    return render(request, 'order_success.html')

# @login_required
# def place_order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#             order.user = request.user
#             order.save()

#             # Update item quantity or delete item
#             item_id = request.POST.get('product_id')
#             quantity = int(request.POST.get('quantity', 1))
#             item = get_object_or_404(Item, pk=item_id)
#             item.quantity -= quantity
#             if item.quantity <= 0:
#                 item.delete()
#             else:
#                 item.save()

#             # Render order success template
#             return render(request, 'order_success.html')
#     else:
#         form = OrderForm()
#     return render(request, 'detailed_product_page.html', {'form': form})
