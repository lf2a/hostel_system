# django
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# local django
from client.models import User


class UserModelForm(ModelForm):
    """
    For update user info
    """

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'mobile_phone', ]


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'mobile_phone',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'mobile_phone',)
