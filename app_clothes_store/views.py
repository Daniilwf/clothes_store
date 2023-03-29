from django.http import HttpResponse
from .models import Cloth
from django.shortcuts import render


def load_name(request):
    latest_cloth_list = Cloth.objects.all()
    output = ', '.join([cloth.name_of_cloth for cloth in latest_cloth_list])
    return HttpResponse(output)


def display_images(request):
    # getting all the objects of hotel.
    allimages = Cloth.objects.all()
    print(allimages)
    data = {"Cloth": allimages}
    return render(request, 'image.html', context=data)
