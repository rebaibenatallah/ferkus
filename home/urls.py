from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='index'),
    # path('ecommerce',views.ecommerce,name='ecommerce'),
]