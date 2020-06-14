# django
from django import forms

# local django
from booking.models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start', 'finish']
        widgets = {'start': DateInput(), 'finish': DateInput()}
