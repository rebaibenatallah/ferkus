
# Ferkus

#### Create Home App
>
> python manage.py startapp home
>
#### 1 - add home app in settings.py>installapp 
>[ home.apps.HomeConfig ]
#### 2 - urls project 
> path('home/',include("home.urls")),
#### 3 - urls home
>from django.urls import path
>
>from . import views
>
>urlpatterns = [
>
>    path('',views.index,name='index'),
>
>]
### 4 - create templates folder and add in settings.py>templates
>
>'DIRS': [os.path.join(BASE_DIR,'templates')],
>
### 5 - create tarjama model
>class tarjama(models.Model):
>    title = models.CharField(max_length=255)
>    text = models.TextField()
>    date = models.DateField()
### show name modle in admin
>from django.contrib import admin
>
>admin.site.register(tarjama)
### show markdown content
install markdown 
> python -m pip install markdown  
then import in views
>import markdown
>
and used in request
>def home(request):
>    md =markdown.Markdown(extensions=["fenced_code"])
>    select = tarjama.objects.first()
>    select.text = md.convert(select.text)
>    context = {"select":select}
>    return render(request,'index.html',context=context)
>
### 6 static 
the first step add static in setting
>STATIC_ROOT = os.path.join(BASE_DIR,'static')
>STATIC_URL = 'static/'
>STATICFILES_DIRS = [
>    os.path.join(BASE_DIR,'ferkus/static'),
>    os.path.join(BASE_DIR,'home/static'),
>]
>
then creat static folder in project folder
>
at the last use in your templets
> {% load static %}
> static 'link file'
>
### 7 - midea
the first step add midea in setting 
>MEDIA_ROOT = os.path.join(BASE_DIR,'media')
>MEDIA_URL = '/media/'
>
then add this line in urls project
>] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>
### 8 - get data from mode
in view page 
>
>obj = Tarjama.objects.all()
>return render(request,'user/tarjama_update.html',{'obj':obj})
>
show this data in templet
>
>{% for x in obj %}
><li><a href="{% url 'tarjama_update2' x.id  %}">{{x.id}}</a></li>
>{% endfor%}
>

### This Step
#### now we are creating models for tarjama this model contains text (markdown) 
