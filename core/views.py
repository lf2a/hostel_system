# django
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate, logout

# local django
from core.forms import ContactForm
from client.forms import CustomUserCreationForm


class HomePageView(TemplateView):
    template_name = 'core/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["form"] = ContactForm()
        return self.render_to_response(context)


class ContactView(FormView):
    http_method_names = ['post']
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def http_method_not_allowed(self, request, *args, **kwargs):
        return redirect('index')

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.add_message(self.request, messages.SUCCESS, 'Email successfully sent!')
        return super().form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.add_message(self.request, messages.ERROR, 'Error sending email')
        return super().form_invalid(form, *args, **kwargs)


class LogoutView(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('index')


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'

    def post(self, request, *args, **kwargs):
        self.object = None
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(self.request, messages.SUCCESS, 'Account successfully created!')
            return redirect('login')
        return super().post(request, *args, **kwargs)
