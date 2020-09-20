from django.shortcuts import render


# Create your views here.
def view_poll(request):

    return render(request, 'poll/poll.html')
