from django.http import HttpResponse
from .models import Cloth
from django.shortcuts import render, redirect
from django.views.generic import DetailView
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail


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


class NewClothesStore(DetailView):
    model = Cloth.objects.all()
    templates_name = 'details_views.html'
    context_object_name = 'mass'


def get_queryset(self):
    return super().get_queryset().filter()


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }
        message = '''
        New message: {}

        From: {}
        '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['scottishcoderdjango@gmail.com'])
    return render(request, 'contact.html')


def register(request):
    form = None
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с єтим адресом уже зарегестрирован!')
        else:
            if form.is_valid():
                ins = form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                user = authenticate(username=username, password=password, email=email)
                ins.email = email
                ins.save()
                form.save_m2m()
                messages.success(request, 'Вы успешно заресестрировались')
                return redirect('/')


    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)



def login(request):
    return render(request, 'login.html')
