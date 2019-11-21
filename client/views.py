# django library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.urls import reverse_lazy
from django.core.paginator import Paginator

# local django
from .models import User, Notification
from .forms import UserForm
from hostel.settings import NUM_OF_ELEMENTS


@login_required
def view_info(request):
    client = User.objects.get(id=request.user.id)

    return render(
        request=request,
        template_name='info.html',
        context={
            'user': client
        }
    )


class UpdateInfo(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        client = User.objects.get(id=request.user.id)

        user_form = UserForm(request.POST or None, instance=client)

        return render(
            request=request,
            template_name='update.html',
            context={
                'form': user_form,
                'user': request.user
            }
        )

    def post(self, request, *args, **kwargs):
        client = User.objects.get(id=request.user.id)

        user_form = UserForm(request.POST or None, instance=client)

        if user_form.is_valid():
            user_form.save()

            return redirect('user_info')

        else:
            return redirect('update_info')


class Delete(LoginRequiredMixin, View):
    template_name = 'delete.html'

    def get(self, request, *args, **kwargs):
        return render(
            request=request,
            template_name='delete.html'
        )

    def post(self, request, *args, **kwargs):
        client = User.objects.get(id=request.user.id)
        client.delete()

        return redirect('logout')


@login_required
def notification(request):
    notifications = Notification.objects.filter(client__id=request.user.id)

    paginator = Paginator(notifications, NUM_OF_ELEMENTS)
    page = request.GET.get('p')
    data = paginator.get_page(page)

    return render(
        request=request,
        template_name='notifications.html',
        context={
            'data': data
        }
    )


@login_required
def get_notification(request, id):
    notification = get_object_or_404(Notification, id=id)

    return render(
        request=request,
        template_name='notification.html',
        context={
            'title': notification.title,
            'description': notification.description,
            'created': notification.created_at
        }
    )
