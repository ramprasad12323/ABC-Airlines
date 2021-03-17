from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User_Data,Book_Data
import random
import requests

username = ""

def home(request):
    return HttpResponseRedirect("/login/")

def login(request):
    return render(request,"Login.html", {})

def regist_user(request):
    return render(request,"Registration.html", {})

def inv_pass(request):
    return render(request,"InvPass.html", {})

def user_notpresent(request):
    return render(request,"UserNotPresent.html", {})

def user_there(request):
    return render(request,"UserThere.html", {})

def sucess_reg(request):
    return render(request,"SucessReg.html", {})

def bookticket(request):
    return render(request,"BookTicket.html", {})

def validation(request):
    if request.method =="POST":
        global username
        username = request.POST.get('user')
        password = request.POST.get('pass')

    try:
        if User_Data.objects.filter(pass_email=username)[0].pass_email:
            if User_Data.objects.filter(pass_email=username)[0].pass_pass == password:
                return render(request,"PassHome.html", {'name' : User_Data.objects.filter(pass_email=username)[0].pass_name})
            else:
                return HttpResponseRedirect("/invpass/")
    except IndexError as error:
        return HttpResponseRedirect("/usernotpresent/")

    print([username,password])

def register(request):
    if request.method == "POST":
        pass_name = request.POST.get('pass_name')
        pass_email = request.POST.get('pass_email')
        pass_pass = request.POST.get('pass_pass')
        pass_address = request.POST.get('pass_address')
        pass_contact = request.POST.get('pass_contact')

        if len(User_Data.objects.filter(pass_email=pass_email)) == 1:
            return HttpResponseRedirect("/userpresent/")
        else:
            obj=User_Data(pass_name,pass_email,pass_pass,pass_address,pass_contact)
            obj.save()
            return HttpResponseRedirect("/sucessreg/")
    
def book(request):
    if request.method == "POST":
        date = request.POST.get('date')
        source = request.POST.get('source')
        destination = request.POST.get('destination')
        seat = request.POST.get('seat')
        meal = request.POST.get('meal')
        global username
        pnr = random.randint(10000000,99999999)
        while len(Book_Data.objects.filter(travel_pnr=pnr))!=0:
            pnr = random.randint(10000000,99999999)
        obj = Book_Data(username,pnr,date,source,destination,seat,meal)
        obj.save()
    return render(request,"PassHome.html", {'name' : User_Data.objects.filter(pass_email=username)[0].pass_name})

def viewticket(request):
    global username
    return render(request,"ViewTicket.html", {'name' : Book_Data.objects.filter(travel_email=username)})
# Create your views here.
