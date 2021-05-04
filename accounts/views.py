from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def about(request):
    html = '<a href="/accounts/index/"> <br>Index</a>'
    return HttpResponse(html)

def index(request):
    html = '<a href="/accounts/about/"> <br>About</a>'
    return HttpResponse(html)