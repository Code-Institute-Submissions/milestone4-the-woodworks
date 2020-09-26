from django.shortcuts import render, redirect, reverse
from django.conf import settings


from .forms import OrderForm
from .models import OrderLineItem
from store.models import Product
from cart.contexts import cart_contents

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    print('pass 1')

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)

        order = order_form.save()
        for item_id, item_data in cart.items():
            product = Product.objects.get(id=item_id)

            order_line_item = OrderLineItem(
                order=order,
                product=product,
                quantity=item_data,
            )
            order_line_item.save()

        return redirect(reverse('checkout_success'))

    else:
        stripe_public_key = settings.STRIPE_PUBLIC_KEY
        stripe_secret_key = settings.STRIPE_SECRET_KEY

        cart = request.session.get('cart', {})
        # Catch users filling out /checkout
        if not cart:
            return redirect(reverse('store'))

        current_cart = cart_contents(request)
        total = current_cart['total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


def checkout_success(request):
    if 'cart' in request.session:
        del request.session['cart']

    return render(request, 'checkout/checkout_success.html')
