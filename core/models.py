# django
from django.db import models
from django.utils.timezone import now

# local django
from client.models import User
from bedroom.models import Bedroom


class Booking(models.Model):
    client = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Client'
    )

    bedroom = models.OneToOneField(
        Bedroom,
        on_delete=models.CASCADE,
        verbose_name='Bedroom'
    )

    total = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='Total'
    )
    start = models.DateField(default=now, verbose_name='Start')
    finish = models.DateField(default=now, verbose_name='Finish')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[ %s ] %s %s' % (
            self.client.username,
            self.bedroom.number,
            self.bedroom.floor
        )

    class Meta:
        ordering = ['-updated_at']
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookigns'
