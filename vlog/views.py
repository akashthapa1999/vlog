from django.http import HttpResponse
from django.shortcuts import render,redirect
from vlogapp.models import vlogDetails


def header(request):
    return render(request, 'header.html')


def footer(request):
    print("jfj")
    if request.method =="POST":
        fname = request.POST["fname"]
        lname =request.POST["lname"]
        date = request.POST["table_date"]
        img = request.POST["img"]
        email = request.POST["table_email"]
        message = request.POST["thought"]
   
        data = vlogDetails(first_name=fname,last_name= lname,Date = date,img=img,email =email,thought = message)
        data.save()

        return redirect(index)
    return render(request, "index.html")


def index(request):
    vlogdata = vlogDetails.objects.all()

    return render(request, 'index.html',{"vlog":vlogdata})