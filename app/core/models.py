"""
Database models.
"""
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

# Create your models here.

class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, phone_number, password=None, **extra_fields):
        """Create, save and return a new user."""

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True) #active users
    is_staff = models.BooleanField(default=False) #login with django admin

    objects = UserManager()

    USERNAME_FIELD = 'phone_number' #phone number is a unique identifier