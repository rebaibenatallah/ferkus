from django.urls import path
from . import views

urlpatterns = [
    path('index',views.home,name='index'),
    # =================== pages ======================
    path('tarjama',views.tarjama_view,name='tarjama'),
    path('objectifs',views.objectifs_view,name='objectifs'),
    path('contact',views.contact_view,name='contact'),
    path('articles-mois',views.articles_mois_view,name='articles_mois'),
    # path('tarjama',views.tarjama_view,name='tarjama'),
    # ================== end pages ===================

    # ==================== user ======================
    path('user',views.home_user,name='user'),
    path('tarjama_form',views.tarjama_form_view,name='tarjama_form'),
    path('tarjama_update',views.tarjama_update_view ,name='tarjama_update'),
    path('tarjama_update/<int:id>',views.tarjama_update_view2 ,name='tarjama_update2'),
    path('contact_user',views.contact_user ,name='contact_user'),
    # ================== end user ====================

]