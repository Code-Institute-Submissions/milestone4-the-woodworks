from django.shortcuts import render
from .models import Poll


# Create your views here.
def view_poll(request):

    poll_product_list = Poll.objects.all()
    template = 'poll/poll.html'
    context = {
        'poll_product_list': poll_product_list
    }

    return render(request, template, context)
