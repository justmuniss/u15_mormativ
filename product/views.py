from django.shortcuts import render, get_object_or_404
from .models import Product,Category
from .forms import ContactForm

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product/list.html', context)


def category_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'category/list.html', context)


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'category/products.html', context)


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return render(request, 'success.html')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)