from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

# Create your models here.

class UserManager(BaseUserManager):
    """Manager for Users"""
    # extra_fields - can be any number of keyword args 
    def create_user(self, email, password=None, **extra_fields):
        """create save and return user"""
        noramlizedEmail = self.normalize_email(email)
        user = self.model(email=noramlizedEmail, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """System Users"""
    def __str__(self):
        return self
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # define which field is used as the username
    USERNAME_FIELD = 'email'