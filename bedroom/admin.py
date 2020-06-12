# django
from django.contrib import admin

# django local
from bedroom.models import Bedroom, BedroomImage


@admin.register(Bedroom)
class BedroomAdmin(admin.ModelAdmin):
    list_display = ('number', 'floor', 'bathroom', 'bed', 'daily', 'created_at', 'last_update', 'is_available',)
    fieldsets = (
        ('Bedroom Info', {
            'classes': ('wide',),
            'fields': ('number', 'floor', 'bathroom', 'bed', 'daily', 'is_available')
        }),
    )


@admin.register(BedroomImage)
class BedroomImageAdmin(admin.ModelAdmin):
    list_display = ('bedroom', 'url', 'created_at', 'last_update',)
    fieldsets = (
        ('Bedroom Image Info', {
            'classes': ('wide',),
            'fields': ('url', 'bedroom')
        }),
    )
