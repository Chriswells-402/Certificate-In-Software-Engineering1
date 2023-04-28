from django.db import models

# Creating  my  models 

class Reg_form(models.Model):
    firstname = models.CharField(max_length=22 )
    lastname = models.CharField(max_length=22 )
    gender = models.CharField(max_length=6)
    country = models.CharField(max_length=22 )
    state = models.CharField(max_length=22 )
    town = models.CharField(max_length=22 )
    email = models.CharField(max_length=22 )
    zipcode = models.CharField(max_length=22 )
    num1 = models.IntegerField(default=0, null=True, blank=True )
    num2 = models.IntegerField(default=0, null=True, blank=True )
    date = models.DateField()