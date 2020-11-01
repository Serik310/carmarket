from django.db import models
from django.core import validators
import uuid
from django.shortcuts import reverse
from decimal import Decimal
from django.conf import settings
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.core.validators import RegexValidator
from django.db.models.signals import pre_save
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null = True, blank= True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200,null = True)

    def __str__(self):
        return self.name
class CarType(models.Model):
    carBrand = models.CharField(max_length=150, verbose_name='Марка', default=None, null=True, blank=True)
    carModel = models.CharField(max_length=100, verbose_name='Модель', default=None, null=True, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.carBrand,self.carModel)

class Car(models.Model):
    ENGINE_TYPES = (
        ('Дизель','Дизель'),
        ('Бензин','Бензин'),
        ('Газ','Газ'),
    )
    TRANSMISSION_TYPE = (
        ('Механика', 'Механика'),
        ('Автомат', 'Автомат')
    )
    id = models.AutoField(primary_key=True, verbose_name='id')
    img = models.ImageField(verbose_name= 'Главная фотка',null = True, upload_to='images/%Y/%m/%d/', height_field=None,width_field=None,max_length=255)
    user_create = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    year = models.PositiveIntegerField(verbose_name = 'Год выпуска')
    carTitle = models.ForeignKey('CarType',on_delete=models.SET_NULL, null=True, verbose_name='Название')
    desc = models.TextField(max_length=1500,verbose_name= 'Описание', null=True, blank=True)
    price = models.PositiveIntegerField(verbose_name = 'Цена')
    engine = models.CharField(max_length=100,verbose_name= 'Тип Движка', choices= ENGINE_TYPES)
    phone_regex = RegexValidator(regex=r"^\+(?:[0-9]●?){6,14}[0-9]$", message=("Неверный формат"))
    contact = models.CharField(validators=[phone_regex], verbose_name=("Номер телефона"), max_length=17, blank=True, null=True)
    date_publication = models.DateTimeField(auto_now_add = True, verbose_name= 'Опубликовано', blank= True, null= True)
    mileage = models.PositiveIntegerField(verbose_name = 'Пробег')
    city = models.CharField(max_length=150, verbose_name= 'Город')
    transmission = models.CharField(max_length=10, verbose_name= 'Коробка Передач', choices=TRANSMISSION_TYPE, default='M')
    adverted = models.BooleanField("Is adverted",default=False)
    class Meta(object):
        ordering = ['-date_publication']
    def __str__(self):
        return str(self.carTitle)

class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'images/%Y/%m/%d/')

    def __str__(self):
        return (str(self.car.carTitle) + ' ' + str(self.car.id))

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add= True)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.order_item_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        total = self.order_item_set.all().count()
        return total

class Order_item(models.Model):
    product = models.ForeignKey(Car,on_delete=models.SET_NULL,null=True)
    date_added = models.DateTimeField(auto_now_add = True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)

    @property
    def get_total(self):
        total = self.product.price
        return total


class Ship_adress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null=True )
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    adress = models.CharField(max_length=200, null=False) 
    city = models.CharField(max_length=200, null=False)  
    state = models.CharField(max_length=200, null=False)  
    zipcode = models.CharField(max_length=200, null=False)  
    date_added = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.adress

# Create your models here.

