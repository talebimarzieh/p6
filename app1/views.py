from django.shortcuts import render
from .models import person
# Create your views here.
def home(request):
    if request.method=="POST":
     n=request.POST.get("name")
     f=request.POST.get("family")
     person.objects.create(name=n,family=f)
    return render(request,"app1/index.html")