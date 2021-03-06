from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_user(self,email,number,name,password,gender,dob,**other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email,number=number,name=name, gender=gender, dob=dob,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,number,name,password,gender,dob,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_active',True)
        other_fields.setdefault('is_superuser',True)
        return self.create_user(email=email, number=number, name=name,password=password, gender=gender, dob=dob,**other_fields)

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    number = models.CharField(unique=True,max_length=10)
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True,blank =True)
    gender = models.CharField(max_length=255)
    dob = models.DateField()
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['number','name','gender','dob']

    objects = CustomAccountManager()

    def __str__(self):
        return self.email

class detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    qualification_certificate = models.ImageField()
    workexperience = models.CharField(max_length=255)
    college_passed_outdate = models.DateField()
    office_name = models.CharField(max_length=255)

    def __str__(self):
        return self.user
 
