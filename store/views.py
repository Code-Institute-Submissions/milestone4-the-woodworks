from django.shortcuts import render
from .models import Product


# Create your views here.
def store(request):
    """
    This view will pass all product objects in the database
    to render the store page.
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'store/store.html', context)
