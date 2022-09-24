from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .models import UsersPhone
from .forms import UsersPhoneForm


# Create your views here.
def HeadMain(request):
    return render (request, 'tel_giude/index.html')

class UsersPhoneCreateView(CreateView):
    template_name = 'tel_giude/add_user.html'
    form_class = UsersPhoneForm
    model = UsersPhone
    success_url = '/guides_phones'

class UsersPhoneListView(ListView):
    model = UsersPhone
    template_name = 'tel_giude/all_users.html'
    context_object_name = 'users_list'

class UsersPhoneDetailView(DetailView):
    model = UsersPhone
    template_name = 'tel_giude/one_user.html'
    context_object_name = "user" 

class UsersPhoneUpdateView(UpdateView):
    model = UsersPhone
    form_class = UsersPhoneForm
    template_name = 'tel_giude/update_user.html'
    context_object_name = "user" 
    success_url = '/guides_phones'
