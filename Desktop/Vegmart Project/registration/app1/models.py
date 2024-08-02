from django.db import models
 
# Create your models here.
class SignUp(models.Model):
    uname=models.CharField(max_length=50)
    email=models.EmailField()
    mobile=models.IntegerField()
    pass1=models.CharField(max_length=50)
    pass2=models.CharField(max_length=50)
    
    
    

   