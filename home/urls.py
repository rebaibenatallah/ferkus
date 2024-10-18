from django.urls import path
from . import views

urlpatterns = [
    path('index',views.home,name='index'),
    # =================== pages ======================
    path('tarjama',views.tarjama_view,name='tarjama'),
    path('objectifs',views.objectifs_view,name='objectifs'),
    # path('tarjama',views.tarjama_view,name='tarjama'),
    # ================== end pages ===================

    # ==================== user ======================
    path('user',views.home_user,name='user'),
    path('tarjama_form',views.tarjama_form_view,name='tarjama_form')
    # ================== end user ====================

]