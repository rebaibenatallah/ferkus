# Ferkus

#### Create Home App
>
> python manage.py startapp home
>
#### 1 - add home app in settings.py>installapp [ home.apps.HomeConfig ]
#### 2 - urls project 
> path('home/',include("home.urls")),
#### 3 - urls home
>from django.urls import path
>from . import views
>
>urlpatterns = [
>    path('',views.index,name='index'),
>]
### This Step
#### now we are creating models for tarjama this model contains text (markdown) 
