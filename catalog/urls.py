from django.urls import path
from catalog import views
from .views import Car_detail, PostCreateView
from django.urls import include
from django.conf.urls import url
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<slug>',Car_detail.as_view(),  name = 'product'),
    path('register/',views.register_page, name = 'register'),
    path('product/new/',PostCreateView.as_view(), name = 'create'),
]