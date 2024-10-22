from django.shortcuts import render
import markdown
from .models import Tarjama ,Contact , art_mois,art_mois_tahmich,image_art
from .forms import Tarjama_form,Contact_form , article_mois_form
# Create your views here.

def home(request):
    return render(request,'index.html')

# ================== pages =================

def tarjama_view(request):
    md =markdown.Markdown(extensions=["fenced_code"])
    select = Tarjama.objects.first()
    select.text = md.convert(select.text)
    context = {"select":select}
    return render(request,'pages/tarjama.html',context=context)

def objectifs_view(request):
    return render(request,'pages/objectifs.html')

def contact_view(request):
    if request.method == 'POST':
        print(request.POST)
        dataform = Contact_form(request.POST)
        if dataform.is_valid():
            dataform.save()
    return render(request,'pages/contact.html')

def articles_mois_view(request):
    objs = art_mois.objects.all()
    return render(request,'pages/articles-mois.html',{'objs':objs})

def articles_mois_view2(request,id):
    md =markdown.Markdown(extensions=["fenced_code"])
    obj_selected = art_mois.objects.get(pk=id)
    obj_selected.text = md.convert(obj_selected.text)
    return render(request,'pages/articles-mois2.html',{'obj_selected':obj_selected})
# ================ end pages ===============

# ==================== user ======================

def home_user(request):
    return render(request,'user/index.html')

def tarjama_form_view(request):
    if request.method == 'POST':
        y = request.POST.get('title')
        x = request.POST.get('text')
        dataform = Tarjama_form(request.POST)
        print(y)
        print(x)
        print(dataform)
        if dataform.is_valid():
            dataform.save()
    return render(request,'user/tarjama.html')

def tarjama_update_view(request):
    obj = Tarjama.objects.all()
    return render(request,'user/tarjama_update.html',{'obj':obj})

def tarjama_update_view2(request,id):
    obj = Tarjama.objects.all()
    obj_selected = Tarjama.objects.get(pk=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        print(obj_selected.title)
        obj_selected.title = title
        obj_selected.text = text
        obj_selected.save()
    return render(request,'user/tarjama_update.html',{'obj':obj,'objselected':obj_selected})

def contact_user(request):
    obj = Contact.objects.all()
    return render(request,'user/contact_user.html',{'contacts':obj})

def article_mois_user_view(request):
    objs = art_mois.objects.all()
    form = article_mois_form()
    if request.method == "POST":
        print(request.POST)
        form = article_mois_form(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
    return render(request,'user/article_mois_user.html',{'objs':objs,'form':form})

def article_mois_update_user_view(request,id):
    objs_img = image_art.objects.all()
    objs = art_mois.objects.all()
    obj_selected = art_mois.objects.get(pk=id)
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        # print(obj_selected.title)
        obj_selected.title = title
        obj_selected.text = text
        obj_selected.save()
    return render(request,'user/article_mois_update_user.html',{'objs':objs,'obj':obj_selected,'imgs':objs_img})

def image_art_user_view(reqest):
    if reqest.method =='POST':
        name = reqest.POST.get('name')
        image = reqest.FILES.get('img')
        link = '![Alt text]('+ name +')'
        data = image_art(name=name,image=image,link=link)
        # if data.is_valid():
        data.save()
        data_u = image_art.objects.get(pk=data.id)
        data_u.link = '![Alt text](http://127.0.0.1:8000/media/' + data.image.name + ')'
        data_u.save()
        print(data.image)
    return render(reqest,'user/image_art_user.html')
# ================== end user ====================