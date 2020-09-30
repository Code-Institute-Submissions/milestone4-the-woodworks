from django.shortcuts import render, redirect
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
    product_type = Poll.objects.all()
    print(product_type)
    redirect_url = request.POST.get('redirect_url')
    Poll[poll_product_id].votes += 1

    return redirect(redirect_url)

