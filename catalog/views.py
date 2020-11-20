import json
import requests

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from django.views.decorators.http import require_POST
from django.db.models.functions import Concat
from django.db.models import Value
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.db.models import Q

from catalog.models import Car, CarImage, Order, Order_item
from catalog.forms import UserRegistrationForm, LoginForm


@require_POST
def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user) 
                return redirect('/')


def index(request):
    catalog_new = Car.objects.all() [:9]
    advert_car = Car.objects.filter(adverted=True)
    advert_car_num = Car.objects.filter(adverted=True).count()
    qs_json = Car.objects.annotate(car_name=Concat(
        'carTitle__carBrand',
        Value(' '),
        'carTitle__carModel'
    )).values_list('car_name', flat=True)
    photos = CarImage.objects.filter(car__in = advert_car)
    photos_num = [x+1 for x in range(photos.count())]

    context={'catalog_new':catalog_new, 
        'advert_car':advert_car,
        'photos': photos,
        'photos_num': photos_num,
        'advert_car_num':advert_car_num, 
        'car_names': ';'.join(list(qs_json))
    }

    return render(
        request,
        'c_shop/index.html',
        context,
    )

def car_detail_view(request, product_id):
    current_product = Car.objects.get(pk = product_id)
    photos_detail = CarImage.objects.filter(car = current_product)
    context = {'current_product': current_product, 
    'photo': photos_detail,
    }
    return render(
        request,
        'c_shop/product.html',
        context
    )

def register_page(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('catalog')
    else:
        form = UserRegistrationForm()
    context = {'form':form}
    return render(
        request,
        'registration/register.html',
        context,
    )

class PostCreateView(CreateView):
    model = Car
    template_name = 'c_shop/create.html'
    fields = ['carTitle','img','year','mileage','engine','city','contact','desc','price','transmission']
    
    def form_valid(self, form):
        form.instance.user_create = self.request.user
        return super().form_valid(form)

def profile(request):
    car_profile = Car.objects.filter(user_create = request.user)
    context = {'car_profile':car_profile}
    return render(
        request,
        'registration/profile.html',
        context,
    )
def shop(request, page_number=1):
    all_cars = Car.objects.all()
    current_page = Paginator(all_cars,2)
    context = {
        'cars':current_page.page(page_number),
    }
    return render(
        request,
        'c_shop/shop.html',
        context,
    )

def about(request):
    return render(
        request,
        'c_shop/about.html',
    )
def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.order_item_set.all()
    else:
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'c_shop/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.order_item_set.all()
    else:
        items = []
    context = {'items': items, 'order': order}
    return render(request, 'c_shop/checkout.html',context)
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ', action)
    print('ProductId: ', productId)
    
    customer = request.user.customer
    product = Car.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    order_item, created = Order_item.objects.get_or_create(order = order, product = product)

    if action == 'remove':
        order_item.delete()
    return JsonResponse('Item was added', safe=False)

def personal_posts(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        post = Car.objects.filter(user_create = customer)
        context = {'post': post}
    return render(request, "c_shop/post.html", context)
