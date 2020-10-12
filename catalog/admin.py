from django.contrib import admin
from .models import Car, CarType

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('carTitle','contact','date_publication','price','user_create')
    list_filter = ('engine','transmission','date_publication')

admin.site.register(CarType)
# Register your models here.
