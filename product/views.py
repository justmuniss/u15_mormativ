from django.shortcuts import render, get_object_or_404,redirect
from .models import Product,Category,Book
from .forms import ContactForm,BookForm

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



def book_list(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'book/list.html', context)

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    context = {
        'book': book
    }
    return render(request, 'book/detail.html', context)


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    context = {
        'form': form
    }
    return render(request, 'book/form.html', context)

def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    context = {
        'form': form
    }
    return render(request, 'book/form.html', context)

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    context = {
        'book': book
    }
    return render(request, 'book/delete.html', context)