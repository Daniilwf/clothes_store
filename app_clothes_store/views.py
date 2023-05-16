from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from .models import Cloth, Client
from .forms import UserForm, ClientForm
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _


def load_name(request):
    latest_cloth_list = Cloth.objects.all()
    output = ', '.join([cloth.name_of_cloth for cloth in latest_cloth_list])
    return HttpResponse(output)


def display_clothes(request):
    # getting all the objects of clothes.
    cloths = Cloth.objects.all()
    return render(request, 'image.html', context={"Cloth": cloths})


def display_user(request):
    # getting all the objects of hotel.
    allimages = Client.objects.all()
    data = {"user": allimages}
    return render(request, 'client.html', context=data)


def load_profile(user):
    try:
        return user.profile
    except:  # this is not great, but trying to keep it simple
        client = Client.objects.create(user=user)
        return client


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        client_form = ClientForm(request.POST, instance=request.user.client)
        if user_form.is_valid() and client_form.is_valid():
            user_form.save()
            client_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return render(request, 'client.html', {'user': request.user})
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        # client_form = Client.objects.create(user=user_form, country=user_form.country, city=user_form.city,
        #                                     address=user_form.address)
        client_form = ClientForm(instance=request.user.client)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'client_form': client_form
    })


def register(response):
    user_form = UserForm(response.POST)
    client_form = ClientForm(response.POST)
    if response.method == 'POST':
        if client_form.is_valid():
            user = user_form.save() + client_form.save()
            client_from = user.client
            user.refresh_from_db()
            user.country = client_form.cleaned_data.get('country')
            user.city = client_form.cleaned_data.get('city')
            user.address = client_form.cleaned_data.get('address')
            user.save()
            username = client_form.cleaned_data.get('username')
            password = client_form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(response, user)

            return redirect('/')

        else:
            user_form = UserForm()
            client_form = ClientForm()

    return render(response, 'register.html', {
        'form': client_form,
        'user_form': user_form
    })


def my_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, 'client.html', context={'user': user})
        # Redirect to a success page.

    else:
        latest_cloth_list = Cloth.objects.all()
        output = ', '.join([cloth.name_of_cloth for cloth in latest_cloth_list])
        return HttpResponse(output)
        # Return an 'invalid login' error message.
