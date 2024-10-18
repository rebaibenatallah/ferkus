from django.urls import path
from . import views

urlpatterns = [
    path('index',views.home,name='index'),
    # =================== pages ======================
    path('tarjama',views.tarjama_view,name='tarjama'),
    path('objectifs',views.objectifs_view,name='objectifs'),
    # path('tarjama',views.tarjama_view,name='tarjama'),
    # ================================================
]