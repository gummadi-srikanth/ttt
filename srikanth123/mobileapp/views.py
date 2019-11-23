from django.shortcuts import render
from django.shortcuts import HttpResponse

def numbers(request):
    return HttpResponse("even numbers")

def home(request):
    return  HttpResponse("Wellcome to django")

def index(request):
    return  HttpResponse("came to mobileapp")

def start (request):
    return  HttpResponse("Start now")

def sri(request):
    return render(request,'sample.html')

def company(request):
    return render(request,"company.html")

def count(request):
    return render(request,'count.html')
