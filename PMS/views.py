from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm,Contactus,PrisonerForm,CellForm
from .models import Today_Top_News,information,Profile,User,Posters,Home_Slide,Prisoner,Cell
from datetime import datetime
from django.contrib import messages




# Create your views here.


def home(request):
    Contact_form = Contactus()
    Slide = Home_Slide.objects
    news = Today_Top_News.objects.order_by('-TopDate')[:20]
    Basic_Info = information.objects.order_by('-id')[:4]
    context = {'news':news,'Basic_Info':Basic_Info, 'Slide':Slide,'Contact_form':Contact_form}
    
   
            
    if request.method == 'POST':
        Contact_form = Contactus(request.POST)
        if Contact_form.is_valid():
            Contact_form.save()
            return render(request, 'PMS/index.html', context)
    else:
        
        return render(request, 'PMS/index.html', context);
    
    
    
    
    if request.method == 'POST':
        if request.method == 'POST':
            Username = request.POST['username']
            Password = request.POST['Password']
            user = authenticate(request, username=Username, password=Password)
            if user is  not None:
                login(request, user)
                messages.success(request, 'You Have Sign In...Welcome!')
                return redirect('detail')
            
            
            else:
                messages.success(request,'Wrong Username or Password try again!')
               
                return render(request, 'PMS/index.html', context);
            

def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,'Account Created for {username}!')
            return redirect('home')
        else:
            form = UserRegisterForm()
            profile_form = ProfileForm()
            context = {'profile_form':profile_form, 'form':form}
            return render(request, 'PMS/Register.html', context)
    else:
        form = UserRegisterForm()
        profile_form = ProfileForm()
        context = {'profile_form':profile_form, 'form':form}
       
        return render(request, 'PMS/Register.html', context)

@login_required   
def detail(request):
    if request.method == 'POST':
        Prisoner_Info = PrisonerForm(request.POST)
        Cell_NameF = CellForm(request.POST)
        if Prisoner_Info.is_valid() and Cell_NameF.is_valid():
            Prisoner_Info.save()
            Cell_NameF.save()
            return render(request, 'PMS/detail.html', context)
        else:
            print ("something wrong")
            Prisoner_Info = PrisonerForm()
            Cell_NameF = CellForm()
            offers = Posters.objects.order_by('-id')[:1]
            context = {'offers':offers, 'Prisoner_Info':Prisoner_Info,'Cell_NameF':Cell_NameF}
            return render(request, 'PMS/detail.html', context)
    else:
        
        Prisoner_Info = PrisonerForm()
        Cell_NameF = CellForm()
        offers = Posters.objects.order_by('-id')[:1]
        context = {'offers':offers, 'Prisoner_Info':Prisoner_Info,'Cell_NameF':Cell_NameF}       

        return render(request, 'PMS/detail.html', context)
    
            
            
  
    

   