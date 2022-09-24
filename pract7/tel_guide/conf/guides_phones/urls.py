from django.urls import path
from .views import HeadMain

urlpatterns = [
        path('', HeadMain, name='Head'),
]