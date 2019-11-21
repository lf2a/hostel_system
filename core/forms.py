# django
from django.forms import ModelForm, DateTimeField, DateInput

# local django
from .models import Booking


class DateInput(DateInput):
    input_type = 'date'


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = [
            'start',
            'finish'
        ]
        widgets = {
            'start': DateInput(),
            'finish': DateInput()
        }
