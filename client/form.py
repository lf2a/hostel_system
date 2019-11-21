from django.contrib.auth.forms import UserCreationForm as CreationForm, UserChangeForm as ChangeForm

from .models import User


class UserCreationForm(CreationForm):
    class Meta(CreationForm):
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'phone1',
            'phone2'
        )


class UserChangeForm(ChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name',
            'phone1',
            'phone2'
        )
