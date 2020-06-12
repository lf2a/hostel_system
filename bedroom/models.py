# django
from django.db import models


class Bedroom(models.Model):
    number = models.IntegerField(verbose_name='Number')
    floor = models.IntegerField(verbose_name='Floor')
    bathroom = models.IntegerField(verbose_name='Bathroom')
    bed = models.IntegerField(verbose_name='Bed')
    daily = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Price per day')
    is_available = models.BooleanField(verbose_name='Is Available', default=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    last_update = models.DateTimeField(auto_now=True, verbose_name='Last Update')

    def __str__(self):
        return 'F%s - N%s' % (self.floor, self.number)

    class Meta:
        ordering = ['floor', 'number']
        verbose_name = 'Bedroom'
        verbose_name_plural = 'Bedrooms'


class BedroomImage(models.Model):
    url = models.ImageField(upload_to='bedroom_images', null=True, blank=True, verbose_name='Bedroom Images')
    bedroom = models.ForeignKey(Bedroom, on_delete=models.CASCADE, verbose_name='Bedroom', related_name='photos',
                                related_query_name='bedroom_photos')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    last_update = models.DateTimeField(auto_now=True, verbose_name='Last Update')

    def __str__(self):
        return 'F%s - N%s' % (self.bedroom.floor, self.bedroom.number)

    class Meta:
        ordering = ['bedroom__floor', 'bedroom__number']
        verbose_name = 'Bedroom Image'
        verbose_name_plural = 'Bedroom Images'
