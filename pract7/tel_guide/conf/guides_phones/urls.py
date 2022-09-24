from django.urls import path
from .views import HeadMain, UsersPhoneCreateView, UsersPhoneListView, \
                    UsersPhoneDetailView, UsersPhoneUpdateView

urlpatterns = [
    path('', HeadMain, name='Head'),
    path('add', UsersPhoneCreateView.as_view(), name='add_user'),
    path('all', UsersPhoneListView.as_view(), name='all_users'),
    path('user/<int:pk>', UsersPhoneDetailView.as_view(), name='one_user'),
    path('user/<int:pk>/update', UsersPhoneUpdateView.as_view(), name='user_update'),
]