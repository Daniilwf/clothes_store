from django.http import HttpResponse
from .models import Cloth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm


def load_name(request):
    latest_cloth_list = Cloth.objects.all()
    output = ', '.join([cloth.name_of_cloth for cloth in latest_cloth_list])
    return HttpResponse(output)


def upload_file(request):
    latest_cloth_list = Cloth.objects.all()
    request.FILES = latest_cloth_list[0].path_to_image
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
