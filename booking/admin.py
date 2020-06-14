# django
from django.contrib import admin

# local django
from booking.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client', 'bedroom', 'start', 'finish', 'total')
    fieldsets = (
        ('booking Info', {
            'classes': ('wide',),
            'fields': ('client', 'bedroom', 'start', 'finish')
        }),
    )
