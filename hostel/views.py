# django
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import generic

# local django
from client.form import UserCreationForm


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def logout_system(request):
    logout(request)
    return redirect('index')


def error_404_view(request, exception):
    data = {
        "msg": "404 Not Found"
    }

    return render(
        request=request,
        template_name='404.html',
        context=data
    )


def error_500_view(request):
    data = {
        'msg': '500 Server Error'
    }

    return render(
        request=request,
        template_name='500.html',
        context=data
    )


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'
