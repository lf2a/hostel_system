# python stl
from datetime import datetime, date

# django
from django.views.generic import (ListView, CreateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# local django
from bedroom.models import Bedroom
from booking.models import Booking
from booking.forms import BookingForm


class BookingListView(LoginRequiredMixin, ListView):
    model = Booking

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        self.object_list = queryset.filter(client=request.user.id)
        return super().get(request=request, *args, **kwargs)


class BookingCreateView(LoginRequiredMixin, CreateView):
    model = Booking
    form_class = BookingForm

    def get(self, request, *args, **kwargs):
        bedroom_id = kwargs.get('id')
        bedroom = Bedroom.objects.get(id=bedroom_id)
        if bedroom.is_available:
            self.object = None
            return super().get(request, *args, **kwargs)
        else:
            messages.add_message(self.request, messages.INFO, 'This room is already booked!')
            return redirect('bedroom', pk=bedroom_id)

    def form_valid(self, form):
        bedroom_id = self.kwargs.get('id')
        # get form start and finish str data and convert to datetime
        fi_obj = datetime.strptime(form.data.get('finish'), '%Y-%m-%d')
        st_obj = datetime.strptime(form.data.get('start'), '%Y-%m-%d')
        days = (fi_obj - st_obj).days
        today_date_obj = date.today()
        # date to datetime
        today = datetime(today_date_obj.year, today_date_obj.month, today_date_obj.day)
        valid_start_date = (st_obj - today).days
        valid_finish_date = (fi_obj - today).days

        if days >= 0 and valid_start_date >= 0 and valid_finish_date >= 0:
            booking = form.save(commit=False)
            bedroom = Bedroom.objects.get(id=bedroom_id)
            booking.bedroom = bedroom
            booking.client = self.request.user
            bedroom.is_available = False
            booking.save()
            bedroom.save()
            messages.add_message(self.request, messages.INFO, 'Reservation made successfully!')
            return redirect('bookings')
        else:
            messages.add_message(self.request, messages.ERROR, 'Error when booking: negative date')
            return redirect('booking_new', id=bedroom_id)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Error when booking.')
        return super().form_invalid(form)


class BookingDeleteView(LoginRequiredMixin, DeleteView):
    model = Booking
    success_url = reverse_lazy('bookings')

    def get(self, request, *args, **kwargs):
        user_id = request.user.id
        user_booking_id = Booking.objects.get(id=kwargs.get('id')).client.id
        if user_id == user_booking_id:
            self.kwargs["pk"] = kwargs.get('id')
            self.object = self.get_object()
            return super().get(request, *args, **kwargs)
        else:
            messages.add_message(self.request, messages.ERROR, 'Action not allowed.')
            return redirect('bookings')

    def post(self, request, *args, **kwargs):
        user_id = request.user.id
        user_booking_id = Booking.objects.get(id=kwargs.get('id')).client.id
        if user_id == user_booking_id:
            self.kwargs["pk"] = kwargs.get('id')
            self.object = self.get_object()
            return super().post(request, *args, **kwargs)
        else:
            messages.add_message(self.request, messages.ERROR, 'Action not allowed.')
            return redirect('bookings')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        bedroom = Bedroom.objects.get(id=self.object.bedroom.id)
        bedroom.is_available = True
        self.object.delete()
        bedroom.save()
        return HttpResponseRedirect(success_url)
