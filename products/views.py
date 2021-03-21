from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db.models import Q
from .forms import ProductForm
from .models import *
from .utils import cookieCart, cartData, guestOrder

# Create your views here.

def index(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    if products:
        return render(request, 'index.html', {'products': products, 'cartItems': cartItems})
    else:
        return render(request, 'index.html', {})


def addProduct(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)

        if product_form.is_valid():
            product_profile = product_form.save(commit=False)

            try:
                product_profile.save()
            except:
                print("Failed to save product_profile!")

            # messages.success(request, _('Your product was successfully saved!'))
            return redirect('index')
        else:
            print("Product_form failed validation")
            pass
            # messages.error(request, _('Correct the errors.'))
    else:
        product_form = ProductForm()

    return render(request, 'add_product.html', {'form': product_form})


def editProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product_form = ProductForm(request.POST, instance=product)

        if product_form.is_valid():
            product_profile = product_form.save(commit=False)

            try:
                product_profile.save()
            except:
                print("Failed to save product profile!")
            # messages.success(request, _('Your profile was successfully updated!'))
            return redirect('index')
        else:
            pass
            # messages.error(request, _('Please correct the errors.'))
    else:
        product_form = ProductForm(instance=product)
        return render(request, 'edit_product.html', {'form': product_form})


def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':
        product.delete()
        return redirect('/')

    return render(request, 'delete_product.html', {'product': product})


def ProductDetails(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product_details.html', {'product': product})


class ProductSearchResults(ListView):
    model = Product
    template_name = 'product_list.html'

    def get_queryset(self, *args, **kwargs):
        val = self.request.GET.get('q')
        if val:
            queryset = Product.objects.filter(
                Q(name__icontains=val) | 
                Q(productCode__icontains=val)
            ).distinct().order_by('name', 'price')
        else:
            queryset = Product.objects.none()
        return queryset


def cart(request):
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems}
    return render(request, 'cart.html', context)