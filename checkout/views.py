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
        'stripe_public_key': 'pk_test_51HVZ9fCslGk1XQYaKPIJ6BiKao5upyhlYgfjqSrcZk1EUkjcPSEZKUto8ihsUrxc0MWEuorpovPhqeRkgQECqY3t00fPkDWgyA',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
