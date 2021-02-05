from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Today_Top_News(models.Model):
        image = models.ImageField(upload_to="images/")
        TopDate = models.DateTimeField(auto_now_add=True,null=False)
        Heading = models.CharField(max_length=150,null=False)
        
        
        def __str__(self):
            return self.Heading
        
class Home_Slide(models.Model):
    SlideImg = models.ImageField(upload_to="images/Slide")
    SlideTitle = models.CharField(max_length=100,null=False)
    TopDate = models.DateTimeField(auto_now_add=True,null=False)
    
    def __str__(self):
            return self.SlideTitle
    
        
class information(models.Model):
    image = models.ImageField(upload_to="images/")
    First_Name = models.CharField(max_length=30,null=False)
    Last_Name = models.CharField(max_length=30,null=False)
    title = models.CharField(max_length=30,null=False)
    Detail = models.CharField(max_length=200,null=False)
    
    def __str__(self):
            return self.title
        
        
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    Idetification_Number = models.CharField(max_length=30,null=False)
    Date_of_Birth = models.DateField(null=False)
    Address = models.CharField(max_length=30,null=False)
    Profile_image = models.ImageField(default='p.jpg', upload_to="images/users", null=True, blank=True)
    
    def __str__(self):
            return self.Idetification_Number
        
class Posters(models.Model):
    offer_destination = models.CharField(max_length=30,null=False)
    sidebar_offer_percent = models.CharField(max_length=8,null=True)
    offer_title = models.CharField(max_length=10,null=False)
    offer_text = models.CharField(max_length=60,null=False)
    image = models.ImageField(default='../PMS/images/89238244.jpg',upload_to="images/offers",null=True)
    Poster_Date = models.DateField(auto_now_add=True,null=False)
    
    def __str__(self):
        
        return self.offer_title
    
class Contactus(models.Model):
    message = models.CharField(max_length=250, null=False)
    name = models.CharField(max_length=40,null=False)
    email = models.CharField(max_length=15,null=True)
    subject = models.CharField(max_length=20, null=False)
    
    def __str__(self):
        
        return self.subject

class Cell(models.Model):
    Cell_ID = models.AutoField(primary_key=True)
    Cell_Name = models.CharField(max_length=6)

class Prisoner(models.Model):
  
    Male = 'M'
    Female = 'F'
    Gender = (
    ('Male', 'MALE'),
    ('Female', 'FEMALE')
        
        )
    
    Prisoner_ID = models.AutoField(primary_key=True)
    First_Names = models.CharField(max_length=60,null=False)
    Surname = models.CharField(max_length=10,null=False)
    DoB = models.DateField(null=False)
    Date_In = models.DateField(auto_now_add=True,null=False)
    Choose_Gender = models.CharField(max_length=6, choices=Gender, default=Male,)
    Status = models.CharField(max_length=10,null=True, default = "Normal")
    Cell_ID = models.ForeignKey(Cell, on_delete=models.CASCADE,null=True)
    

    
    
    
    
    
    
    
class Visitor(models.Model):
    Visitor_ID = models.AutoField(primary_key=True)
    Card_Number = models.CharField(max_length=4,null=False)
    Prisoner_ID = models.OneToOneField(Prisoner, null=False, on_delete=models.CASCADE)


    
class Prison(models.Model):
    Prison_ID = models.IntegerField(primary_key=True)
    Prison_Name = models.CharField(max_length=60,null=False)
    Address = models.CharField(max_length=60,null=False)
    Prison_ID = models.ManyToManyField(Prisoner)
    
class Case(models.Model):
    Case_ID = models.AutoField(primary_key=True)
    Case_Type = models.CharField(max_length=10,null=False)
    Case_year = models.DateField()   
    

 
    
class Prisoner_Case(models.Model):
    Case_ID = models.ManyToManyField(Case)
    Prisoner_ID = models.ManyToManyField(Prisoner)
    




    
    
    
    
    




    
    
    
    

    
    
    

   
        