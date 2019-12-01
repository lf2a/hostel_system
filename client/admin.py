from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UA

from .form import UserCreationForm, UserChangeForm
from .models import User, Notification


class UserAdmin(UA):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active')

    fieldsets = (
        (
            None, {
                'fields': (
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'phone1',
                    'phone2',
                    'password'
                )
            }),
        (
            'Permissions', {
                'fields': ('is_staff', 'is_active')
            }
        ),
    )

    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')
            }
        ),
    )

    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User, UserAdmin)
admin.site.register(Notification)
