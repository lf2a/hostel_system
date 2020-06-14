# python stl
from datetime import datetime

# django
from django.db import models
from django.utils.timezone import now

# local django
from client.models import User
from bedroom.models import Bedroom


class Booking(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Client', related_name='client')
    bedroom = models.OneToOneField(Bedroom, on_delete=models.CASCADE, verbose_name='Bedroom', related_name='bedroom')
    total = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Total')
    start = models.DateField(default=now, verbose_name='Start')
    finish = models.DateField(default=now, verbose_name='Finish')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_days(self):
        days = (self.finish - self.start).days
        return days + 1

    def calc_total(self):
        total = self.get_days() * self.bedroom.daily
        return total

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return '[%s] %s >> N%s - F%s' % (self.total, self.client.username, self.bedroom.number, self.bedroom.floor)
