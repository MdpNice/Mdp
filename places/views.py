from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .forms import PlaceForm

from places.models import Place
from partners.models import PersonByPlace


def place_list(request):
    places = Place.objects.all()
    return render(request, 'places/place_list.html', {'places': places})


def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    personbyplaces = PersonByPlace.objects.filter(place=place)

    return render(request, 'places/place_detail.html', {'place': place, 'personbyplaces': personbyplaces})


def place_add(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = form.save(commit=False)
            place.user = request.user
            place.save()
            return redirect('place_detail', pk=place.pk)
    else:
        form = PlaceForm()
    return render(request, 'places/place_edit.html', {'form': form})


def place_edit(request, pk):
    place = get_object_or_404(Place, pk=pk)

    if request.method == "POST":
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            place = form.save(commit=False)
            place.user = request.user
            place.save()
            return redirect('place_detail', pk=place.pk)
    else:
        form = PlaceForm(instance=place)

    return render(request, 'places/place_edit.html', {'form': form})


def places_get(request):
    places = []
    for obj in Place.objects.all():
        places += [{
            'title': obj.title,
            'lat': float(obj.lat),
            'lng': float(obj.lng)
        }]
    data = {"places": places}
    return JsonResponse({'status':data,})
