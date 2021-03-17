from django.db import models

class User_Data(models.Model):
    pass_name=models.CharField(max_length=50,null=False)
    pass_email=models.EmailField(primary_key=True, unique=True,null=False)
    pass_pass=models.CharField(max_length=50,null=False)
    pass_address=models.TextField(null=False,max_length=200)
    pass_contact=models.CharField(null=False,max_length=10)

class Book_Data(models.Model):
    travel_email=models.EmailField(null=False)
    travel_pnr = models.CharField(primary_key=True, null=False,max_length=12,unique=True)
    travel_date = models.DateField(null=False)
    travel_source = models.CharField(null=False,max_length=50)
    travel_destination = models.CharField(null=False,max_length=50)
    seat_pre = models.CharField(null=False,max_length=10)
    seat_meal = models.CharField(null=False,max_length=10)


# Create your models here.
