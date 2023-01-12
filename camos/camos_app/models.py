from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.contrib.auth.models import UserManager
from django.contrib.auth import get_user, get_user_model

class UserManager(BaseUserManager):
    def create_user(self, username, email, company_name, password=None):
        if not email:
            raise ValueError('Enter Email!')
        user = self.model(
            username = username,
            email = email,
            company_name = company_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, password=None):
        user = self.model(
            username = username,
            email = email,
        )
        user.set_password(password)
        user.company_name = '株式会社camos'
        user.user_type='admin'
        user.is_staff = True
        user.is_active = True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    company_name = models.CharField(max_length=255, unique=True)
    user_type = models.CharField(max_length=10)
    site_name = models.CharField(max_length=255, null=True)
    capital = models.IntegerField(null=True)
    website = models.URLField(null=True)
    permit_license = models.FileField(null=True, upload_to='camos_app/')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    objects = UserManager()
    
    class Meta:
        db_table = 'users'
        
    def __str__(self):
        return self.email
    
class Post(models.Model):
    title = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.IntegerField()
    body = models.TextField()
    agent = models.CharField(max_length=255)
    data_added = models.DateTimeField(auto_now_add=True)
    create_user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    create_user_company = models.CharField(max_length=255)
    
class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    experience = models.BooleanField(default=False, null=True)
    construction1 = models.CharField(max_length=255)
    construction2 = models.CharField(max_length=255)
    construction3 = models.CharField(max_length=255)
    create_user = models.CharField(max_length=255)
    create_user_company = models.CharField(max_length=255)
    result = models.CharField(max_length=255, null=True)
    job = models.ForeignKey(Post, on_delete=models.CASCADE,)
    