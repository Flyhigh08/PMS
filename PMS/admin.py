from django.contrib import admin
from .forms import UserRegisterForm, ProfileForm,Contactus,PrisonerForm
from .models import Today_Top_News,information,Profile,Posters,Home_Slide,Contactus,Prisoner




admin.site.register(Today_Top_News,)
admin.site.register(information)
admin.site.register(Prisoner)
admin.site.register(Profile)
admin.site.register(Posters)
admin.site.register(Home_Slide)
admin.site.register(Contactus)









admin.site.site_header = "PMS Admin DashBoard"
admin.site.index_title = "Prison Management System"






