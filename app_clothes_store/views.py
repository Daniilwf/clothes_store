from django.http import HttpResponse
from .models import Cloth
from django.shortcuts import render
from django.views.generic import DetailView


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

class NewClothes_store(DetailView):
    model = Cloth.objects.all()
    templates_name = 'main/details_views.html'
    context_object_name = 'post'

def get_queryset(self):
    return super().get_queryset().filter()

def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
