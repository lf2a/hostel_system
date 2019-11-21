# django library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views import View
from django.urls import reverse_lazy

# local django
from .models import User, Notification
from .forms import UserForm


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


# @login_required
# def update_info(request):
#     client = User.objects.get(id=request.user.id)

#     user_form = UserForm(request.POST or None, instance=client)

#     if user_form.is_valid():
#         user_form.save()
#         return redirect('user_info')

#     return render(
#         request=request,
#         template_name='update.html',
#         context={
#             'form': user_form,
#             'user': request.user
#         }
#     )


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


# @login_required
# def delete(request):
#     client = User.objects.get(id=request.user.id)

#     if request.method == 'POST':
#         client.delete()
#         return redirect('logout')

#     return render(
#         request=request,
#         template_name='delete.html'
#     )


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

    return render(
        request=request,
        template_name='notifications.html',
        context={
            'data': notifications
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