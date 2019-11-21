# django
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

# local django
from client.models import User
from bedroom.models import Bedroom, BedroomImage
from .models import Booking
from .forms import BookingForm
from hostel.settings import NUM_OF_ELEMENTS

# python standard library
from datetime import datetime, date
import json


@login_required
def bookings(request):
    bookings = Booking.objects.filter(client__id=request.user.id)

    data = []
    for booking in bookings:

        data.append({
            'id': booking.id,
            'client': booking.client,
            'bedroom': booking.bedroom,
            'images': BedroomImage.objects.filter(bedroom__id=booking.bedroom.id),
            'total': booking.total,
            'start': booking.start,
            'finish': booking.finish,
            'created_at': booking.created_at
        })

    paginator = Paginator(data, NUM_OF_ELEMENTS)
    page = request.GET.get('p')
    bks = paginator.get_page(page)

    return render(
        request=request,
        template_name='bookings.html',
        context={
            'data': bks
        }
    )


class BookingDelete(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='booking_delete.html')

    def post(self, request, *args, **kwargs):
        booking = get_object_or_404(Booking, id=self.kwargs['id'])

        if booking.client.id == request.user.id:
            booking.delete()
            return redirect('bookings')
        else:
            return redirect('booking_delete')


@login_required
def booking_create(request):
    if request.method == 'POST':
        client = get_object_or_404(User, id=request.user.id)
        bedroom = get_object_or_404(Bedroom, id=request.POST.get('bedroom'))

        start = request.POST.get('start')
        start_obj = datetime.strptime(start, '%Y-%m-%d')

        finish = request.POST.get('finish')
        finish_obj = datetime.strptime(finish, '%Y-%m-%d')

        days = (finish_obj - start_obj).days
        total = float(bedroom.daily) * days

        booking = Bedroom(
            client=client,
            bedroom=bedroom,
            start=start_obj,
            finish=finish_obj,
            total=total
        )
        booking.save()
        return redirect('bookings')

    return redirect('bedrooms')


class BookingUpdate(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
        booking = get_object_or_404(Booking, id=self.kwargs['id'])

        booking_form = BookingForm(request.POST or None, instance=booking)

        return render(
            request=request,
            template_name='booking_update.html',
            context={
                'form': booking_form,
                'start': booking.start,
                'finish': booking.finish
            }
        )

    def post(self, request, *args, **kwargs):
        booking = get_object_or_404(Booking, id=self.kwargs['id'])

        booking_form = BookingForm(request.POST or None, instance=booking)

        if booking_form.is_valid():
            booking_form.save()

            return redirect('bookings')
        else:
            return redirect('booking_update')
