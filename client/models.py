# django
from django.db import models
from django.contrib.auth.models import AbstractUser

# local django
from client.managers import UserManager


class User(AbstractUser):
    email = models.EmailField('Email', unique=True)
    mobile_phone = models.CharField(max_length=17, verbose_name='Mobile Phone', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    last_update = models.DateTimeField(auto_now=True, verbose_name='Last Update')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['username']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
