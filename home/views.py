from django.shortcuts import render
import markdown
from .models import Tarjama ,Contact
from .forms import Tarjama_form,Contact_form
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
    return render(request,'pages/articles-mois.html')
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
# ================== end user ====================