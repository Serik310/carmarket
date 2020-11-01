from django.urls import path
from catalog import views
from .views import PostCreateView
from django.urls import include
from django.conf.urls import url
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('<int:product_id>/',views.car_detail_view,  name = 'product'),
    path('register/',views.register_page, name = 'register'),
    path('product/new/',PostCreateView.as_view(), name = 'create'),
    path('profile/',views.profile, name = 'profile'),
    path('shop/',views.shop, name = 'shop'),
    path('about/',views.about, name = 'about'),
    path('update_item/',views.updateItem, name ='update_item'),
    path('cart/', views.cart, name = 'cart'),
]