from django.shortcuts import render, redirect, reverse


# Create your views here.
def view_cart(request):

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the product to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


# def adjust_cart(request, id):
#     """
#     Adjust the quantity of the specified product to the specified
#     amount. This function was taken from Rob Simons' MS4.
#     https://github.com/RobSimons1/ms4-ecommerce
#     """
#     print(request.POST)
#     quantity = int(request.POST.get('quantity'))
#     cart = request.session.get('cart', {})
#     redirect_url = request.POST.get('redirect_url')

#     if quantity > 0:
#         cart[id] = quantity
#     else:
#         cart.pop(id)

#     request.session['cart'] = cart
#     return redirect(redirect_url)
