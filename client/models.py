from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=15,
        unique=True,
        verbose_name='Username'
    )
    first_name = models.CharField(
        max_length=30,
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name='Last Name',
        null=True,
        blank=True
    )
    phone1 = models.CharField(
        max_length=17,
        verbose_name='Phone 1',
        null=True,
        blank=True
    )
    phone2 = models.CharField(
        max_length=17,
        verbose_name='Phone 2',
        null=True,
        blank=True
    )
    email = models.EmailField(
        _('Email Address'),
        unique=True
    )

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Notification(models.Model):
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='User'
    )
    title = models.CharField(
        max_length=50,
        verbose_name='Title'
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Description'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created At'
    )

    def __str__(self):
        return '%s' % self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'
