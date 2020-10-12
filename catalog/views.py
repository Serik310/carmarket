from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from .models import Car
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .filters import OrderFilter
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib import messages
from django.core.mail import send_mail

def index(request):
    catalog_new = Car.objects.all()
    advert_car = Car.objects.filter(adverted = True)
    advert_car_num = Car.objects.filter(adverted = True).count()
    myFilter = OrderFilter(request.GET, queryset=catalog_new)
    catalog_new = myFilter.qs
    return render(
        request,
        'c_shop/index.html',
        context={'catalog_new':catalog_new, 'advert_car':advert_car,'advert_car_num':advert_car_num, 'myFilter':myFilter}
    )

class Car_detail(DetailView):
    model = Car
    template_name = "c_shop/product.html"
    def contact(self,request):
        if request.method == "POST":
            messages_email = request.POST['message-email']
            messages_question = request.POST['message-question']
            messages_author_email = self.request.user._meta.get_field('email')
            context = {
                'messages_email':messages_email,
                'messages_author_email':messages_author_email,
                }
            send_mail(
                '',
                messages_question,
                messages_email,
                messages_author_email,
            )
            return(request, self.template_name, context)
        else:
            return(request, self.template_name, {})

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
        form.instance.user = self.request.user
        Car.user_create = self.request.user
        return super().form_valid(form)

# Create your views here.
