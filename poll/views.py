from django.shortcuts import render, redirect, get_object_or_404
from .models import Poll


# Create your views here.
def view_poll(request):

    poll_product_list = Poll.objects.all()
    template = 'poll/poll.html'
    context = {
        'poll_product_list': poll_product_list
    }

    return render(request, template, context)


def add_vote(request, poll_product_id):
    product_type = get_object_or_404(Poll, pk=poll_product_id)
    print(product_type.product_type)
    print(product_type.votes)
    redirect_url = request.POST.get('redirect_url')
    product_type.votes += 1
    product_type.save()

    return redirect(redirect_url)
