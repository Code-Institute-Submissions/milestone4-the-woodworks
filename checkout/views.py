from django.shortcuts import render, redirect, reverse
from .forms import OrderForm

# Create your views here.


def checkout(request):

    cart = request.session.get('cart', {})
    # Catch users filling out /checkout
    if not cart:
        return redirect(reverse('store'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
