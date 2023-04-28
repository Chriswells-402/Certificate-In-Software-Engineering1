from django.shortcuts import render
from .models import Reg_form
from django.contrib import messages
# Create your views here.

def index(request):

    return render(request, 'index.html')

def registration(request):
    first_name = request.POST['firstname']
    last_name = request.POST['lastname']
    Email = request.POSt['email']
    genderr = request.POST['gender']
    countrry = request.POST['country']
    townn= request.POST['gender']
    zip_code = request.POST['zipcode']
    statee = request.POST['state']
    number = request.POST['num1']
    numbers = request.POST['num2']
    dateof = request.POST['date']
    
    Reg_form=[
        first_name,last_name,Email,genderr,countrry,townn,zip_code,statee,number,numbers,dateof
    ]

   
    