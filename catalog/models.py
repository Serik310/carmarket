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
    cId = models.UUIDField(primary_key = True ,verbose_name= 'ID', default = uuid.uuid4)
    img = models.ImageField(verbose_name= 'Главная фотка',null = True, upload_to='images/%Y/%m/%d/', height_field=None,width_field=None,max_length=255)
    user_create = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    year = models.PositiveIntegerField(verbose_name = 'Год выпуска')
    carTitle = models.ForeignKey('CarType',on_delete=models.SET_NULL, null=True, verbose_name='Полное название')
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
    slug = models.SlugField()
    class Meta(object):
        ordering = ['-date_publication']
    def __str__(self):
        return str(self.carTitle)

    def get_absolute_url(self):
        return reverse("core:product", kwargs= {
            'slug': self.slug
        })

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = "cartest"

pre_save.connect(slug_generator, sender=Car)
# Create your models here.

