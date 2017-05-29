from django.shortcuts import render

from .models import MailList
# Create your views here.


def home(request):
    mail = request.POST.get('mail')
    notification = None
    if mail:
        instance = MailList(email=mail)
        instance.save()
        notification = 'You will be notified as soon as we launch the website!'
    context = {'notification': notification}
    return render(request, 'home.html', context)
