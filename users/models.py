from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

# Create your models here.


class User(AbstractUser):
    objects = UserManager()
    email = models.EmailField(_('email address'), unique=True)
    USERNAME_FIELD = 'email'