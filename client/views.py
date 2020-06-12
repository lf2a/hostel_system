# django library
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.views.generic import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# local django
from client.models import User
from client.forms import UserModelForm


class UserProfileTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'client/user_detail_view.html'
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["user"] = User.objects.get(id=request.user.id)
        return self.render_to_response(context)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'client/user_edit_view.html'
    form_class = UserModelForm
    success_url = reverse_lazy('user_detail')
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        self.kwargs["pk"] = request.user.id
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.kwargs["pk"] = request.user.id
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('bedrooms')
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        self.kwargs["pk"] = request.user.id
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.kwargs["pk"] = request.user.id
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)
