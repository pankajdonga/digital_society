from django.db import models

# Create your models here.

class invoice(models.Model):
    created_at=models.DateField(auto_now_add=True)
    charges_type=models.CharField(max_length=100)
    member_name=models.CharField(max_length=100)
    amount=models.IntegerField()
    inv=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField()
    discription=models.TextField()

class AddEvent(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    event_title=models.CharField(max_length=100)
    event_img=models.ImageField(upload_to='profile_img')
    start_date=models.DateField()
    end_date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    description=models.CharField(max_length=200)

class SocietyLogo(models.Model):
    logo=models.ImageField(upload_to='main_logo')
    




