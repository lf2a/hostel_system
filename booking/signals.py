# django
from django.db.models.signals import pre_save
from django.dispatch import receiver

# django local
from booking.models import Booking


@receiver(signal=pre_save, sender=Booking)
def set_total(sender, instance, **kwargs):
    instance.total = instance.calc_total()
