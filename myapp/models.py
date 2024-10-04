from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class CustomBaseManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Please Enter Valid Email Address...')
        
        emai=self.normalize_email(email)
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)
    

class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    mobile=models.BigIntegerField(blank=True, null=True)
    birthdate=models.DateField(blank=True, null=True)
    gender=models.CharField(max_length=20)
    gate=models.CharField(max_length=20,blank=True,null=True)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=20,blank=True,null=True)
    state=models.CharField(max_length=20,blank=True,null=True)
    adhar=models.BigIntegerField(blank=True, null=True)
    profile_img=models.ImageField(upload_to='profile_imgs',blank=True, null=True)
    membertype=models.CharField(max_length=100,blank=True,null=True)

    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=CustomBaseManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def __str__(self):
        return self.email
    


    

