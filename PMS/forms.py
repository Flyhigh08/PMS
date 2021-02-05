from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Contactus,Prisoner,Cell

        
        
class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(required=False)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = [
            'Idetification_Number',
            'Date_of_Birth',
            'Address',
            'Profile_image'
   ]
        

class Contactus(forms.ModelForm):
    message = forms.CharField(max_length=250,required=True)
    name = forms.CharField(max_length=250,required=True)
    email = forms.EmailField(max_length=250,required=False)
    subject = forms.CharField(max_length=250,required=True)

    class Meta:
        model = Contactus
        fields = [
            'message',
            'name',
            'email',
            'subject'
        ]

    
class PrisonerForm(forms.ModelForm):
    
    class Meta:
        
        model = Prisoner
        fields = ['First_Names','Surname','DoB','Choose_Gender','Status']
        
class CellForm(forms.ModelForm):
    Cell_Name = forms.CharField(max_length=6)
    class Meta:
        model = Cell
        fields = [ 'Cell_Name']
    
    
        
    
        