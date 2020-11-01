from django.contrib import admin
from .models import Car, CarType,CarImage, Order, Order_item, Ship_adress,Customer

class CarImageAdmin(admin.StackedInline):
    model = CarImage

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('carTitle','contact','date_publication','price','user_create')
    list_filter = ('engine','transmission','date_publication')
    inlines = [CarImageAdmin]
admin.site.register(CarType)

@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Order)
admin.site.register(Order_item)
admin.site.register(Ship_adress)
admin.site.register(Customer)
# Register your models here.
