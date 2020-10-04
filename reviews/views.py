from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from store.models import Product


# Create your views here.
def view_reviews(request, product_id):
    """"
    Gets the id of the specific product and searches for all reviews
    connect to it and puts them in review_list which is then returned
    to the template (reviews.html)
    """
    product = get_object_or_404(Product, pk=product_id)
    review_list = Review.objects.all().filter(product=product)
    template = 'reviews/reviews.html'
    context = {
        'review_list': review_list,
        'product': product
    }

    return render(request, template, context)


def add_review(request, product_id):
    """
    When the add review button on the page is pressed the function is called
    and given the product_id as an argument.
    """
    selected_product = get_object_or_404(Product, pk=product_id)
    print(selected_product.id)
    redirect_url = request.POST.get('redirect_url')
    return redirect(redirect_url)


# def add_vote(request, poll_product_id):
#     product_type = get_object_or_404(Poll, pk=poll_product_id)
#     print(product_type.product_type)
#     print(product_type.votes)
#     redirect_url = request.POST.get('redirect_url')
#     product_type.votes += 1
#     product_type.save()

#     return redirect(redirect_url)
