from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class Users_profileManager(BaseUserManager):
    def create_user(self, email, name, password):
        if not email:
            raise ValueError('User must have a email')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.save(using=self._db)

        return user

class Users_profile(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    objects = Users_profileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return {self.name}

    def __str__(self):
        return {self.email}
