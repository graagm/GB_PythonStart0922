from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DetailView
from .models import UsersPhone
from .forms import UsersPhoneForm
from rest_framework import parsers as rfpr
from django.views.decorators.csrf import csrf_exempt
from .serializers import UsersPhoneSerializer


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


@csrf_exempt
def users_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = UsersPhone.objects.all()
        serializer = UsersPhoneSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = rfpr.JSONParser().parse(request)
        serializer = UsersPhoneSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = UsersPhone.objects.get(pk=pk)
    except UsersPhone.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UsersPhoneSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = rfpr.JSONParser().parse(request)
        serializer = UsersPhoneSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)