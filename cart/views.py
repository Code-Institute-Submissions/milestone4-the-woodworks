from django.shortcuts import render, redirect


# Create your views here.
def view_cart(request):

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the product to the cart """
    redirect_url = request.POST.get('redirect_url')
    
    if request.POST.get('quantity'):
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        if quantity <= 5 and quantity > 0:
            if item_id in list(cart.keys()):
                if cart[item_id] + quantity <= 5:
                    cart[item_id] += quantity
                else:
                    return redirect(redirect_url)
            else:
                cart[item_id] = quantity

            request.session['cart'] = cart
            return redirect(redirect_url)
        else:
            return redirect(redirect_url)
    else:
        return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Add a quantity of the product to the cart """
    redirect_url = request.POST.get('redirect_url')

    if request.POST.get('quantity'):
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
        if quantity > 0 and quantity <= 5:
            if quantity > 0:
                cart[item_id] = quantity
            else:
                cart.pop(item_id)

            request.session['cart'] = cart
            return redirect(redirect_url)
        else:
            return redirect(redirect_url)
    else:
        return redirect(redirect_url)

