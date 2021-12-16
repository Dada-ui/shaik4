from django.http import HttpResponse
from django.shortcuts import render

def manually(request):
    x = open(r"C:\Users\SHAIK\Desktop\shaik\s\sample.html","rb")
    y = x.read()
    return HttpResponse(y)

def automatically(request):
    return render(request,"home.html")