from django.shortcuts import render
import markdown
from .models import Tarjama
from .forms import Tarjama_form
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

# ================== end user ====================