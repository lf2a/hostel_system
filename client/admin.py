# django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# local django
from client.forms import CustomUserCreationForm, CustomUserChangeForm
from client.models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('username', 'first_name', 'last_name', 'mobile_phone', 'email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')

    fieldsets = (('Info', {'fields': ('username', 'first_name', 'last_name', 'email', 'mobile_phone', 'password',)}),
                 ('Permissions', {'fields': ('is_staff', 'is_active')}),)

    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username', 'email', 'password1', 'password2', 'is_staff')}),)

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
