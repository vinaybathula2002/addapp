from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request,'add.html')
def addition(request):
    x=int(request.POST["t1"])
    y=int(request.POST["t2"])
    z=x+y
    return HttpResponse("the sum is:"+str(z))


# Create your views here.
