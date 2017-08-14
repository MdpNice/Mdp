from django.shortcuts import render

from django.contrib.auth.models import User
from partners.models import Partner
from places.models import Place


def home(request):
    return render(request, 'home/home.html', {})


def stats(request):

    partnercount = Partner.objects.all().count()
    placecount = Place.objects.all().count()
    usercount = User.objects.all().count()

    return render(
        request,
        'home/stats.html', {
            'partnercount': partnercount,
            'usercount': usercount,
            'placecount': placecount,
        })
