from django.http import HttpResponse
from django.views.decorators.http import require_POST

from .cart import Cart
from .models import Cloth, Favorite
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, CartAddProductForm
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail


def load_name(request):
    latest_cloth_list = Cloth.objects.all()
    output = ', '.join([cloth.name_of_cloth for cloth in latest_cloth_list])
    return HttpResponse(output)


def main(request):
    # getting all the objects of hotel.
    cloth_with_discount = Cloth.objects.exclude(price_with_discount=0).order_by('?')[:4]
    cloth_without_discount = Cloth.objects.filter(price_with_discount=0).order_by('?')[:4]
    data = {"cloth_with_discount": cloth_with_discount, "cloth_without_discount": cloth_without_discount}
    return render(request, 'Главная.html', context=data)


class NewClothesStore(DetailView):
    model = Cloth
    template_name = 'товар.html'
    context_object_name = 'cloth'

    def get_queryset(self):
        return super().get_queryset().filter()

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm
        return context


def about(request):
    return render(request, 'О-нас.html')


def discounts(request):
    cloth_with_discount = Cloth.objects.exclude(price_with_discount=0).order_by('?')
    return render(request, 'скидки.html', {"cloth_with_discount": cloth_with_discount})


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
            messages.error(request, 'Пользователь с этим адресом уже зарегестрирован!')
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


def assortment(request):
    all_clothes = Cloth.objects.all()
    form = CartAddProductForm()
    return render(request, 'Ассортимент.html', {"all_clothes": all_clothes, "cart_product_form": form})


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Cloth, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('CartDetail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Cloth, id=product_id)
    cart.remove(product)
    return redirect('CartDetail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'quantity': item['quantity'],
                'update': True
            })
    return render(request, 'корзина.html', {'cart': cart})


def output_favorites(request):
    if request.user.is_authenticated:
        favorites = Favorite.objects.filter(user=request.user)
    else:
        favorites = None
    return render(request, 'Избранное.html', {'all_clothes': favorites})


def add_to_favorite(request, cloth_id):
    cloth = Cloth.objects.get(id=cloth_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, cloth=cloth)
    return redirect('mass-detail', pk=cloth_id)


def delete_from_favorite(request, cloth_id):
    cloth = Cloth.objects.get(id=cloth_id)
    favorite = Favorite.objects.filter(user=request.user, cloth=cloth).first()
    if favorite is not None:
        favorite.delete()
    return redirect('mass-detail', pk=cloth_id)
