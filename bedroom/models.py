# django
from django.db import models


class Bedroom(models.Model):
    number = models.CharField(max_length=10, verbose_name='Number')
    floor = models.IntegerField(verbose_name='Floor')
    bathroom = models.IntegerField(verbose_name='Bathroom')
    bed = models.IntegerField(verbose_name='Bed')
    daily = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='Daily Price'
    )

    def __str__(self):
        return '[ %s ] %s' % (self.floor, self.number)


class BedroomImage(models.Model):
    url = models.ImageField(
        upload_to='bedroom_images',
        null=True,
        blank=True,
        verbose_name='Bedroom Images'
    )

    bedroom = models.ForeignKey(
        Bedroom, on_delete=models.CASCADE, verbose_name='Bedroom')

    def __str__(self):
        return '[ %s ] %s' % (self.bedroom.floor, self.bedroom.number)
