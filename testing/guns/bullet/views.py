from django.shortcuts import render
from django.shortcuts import HttpResponse
def home(request):
    return render(request,'home.html')

def addition(request):
    val1=request.POST.get('num1')
    val2=request.POST.get('num2')
    res=int(val1)+int(val2)
    return render(request,'result.html',{'result':res})


# Create your views here.
