from django.shortcuts import render
from app.models import Cinema
from app.forms import cinemaform
# Create your views here.
def view(request):
    b=Cinema.objects.all()
    return render(request,'view.html',{'c':b})

def add(request):
    if(request.method=="POST"):
        n=request.POST['n']
        y=request.POST['y']
        r=request.POST['r']
        g=request.POST['g']
        i=request.FILES['i']
        b=Cinema.objects.create(name=n,year=y,rating=r,genre=g,image=i)
        b.save()
        return view(request)
    return render(request,'add.html')

def add1(request):
    form=cinemaform()
    if(request.method=="POST"):
        form=cinemaform(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return view(request)
    return render(request,'add1.html',{'form':form})

def view1(request,p):
    b=Cinema.objects.get(id=p)
    return render(request,'view1.html',{'c':b})

def deleteby1(request,p):
    b=Cinema.objects.get(id=p)
    b.delete()
    return view(request)

def editby1(request,p):
    b=Cinema.objects.get(id=p)
    form=cinemaform(instance=b)
    if(request.method=="POST"):
        form=cinemaform(request.POST,request.FILES,instance=b)
        if form.is_valid():
            form.save()
            return view(request)
    return render(request,'add1.html',{'form':form})