from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .models import UsersPhone


# Create your views here.
def HeadMain(request):
    return render (request, 'tel_giude/index.html')