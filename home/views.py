from django.shortcuts import render
from .models import tarjama
import markdown
# Create your views here.

def home(request):
    md =markdown.Markdown(extensions=["fenced_code"])
    select = tarjama.objects.first()
    select.text = md.convert(select.text)
    context = {"select":select}
    return render(request,'index.html',context=context)