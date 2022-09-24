from django.urls import path
from .views import HeadMain, UsersPhoneCreateView, UsersPhoneListView, \
                    UsersPhoneDetailView, UsersPhoneUpdateView,\
                    users_list, user_detail


urlpatterns = [
    path('', HeadMain, name='Head'),
    path('add', UsersPhoneCreateView.as_view(), name='add_user'),
    path('all', UsersPhoneListView.as_view(), name='all_users'),
    path('user/<int:pk>', UsersPhoneDetailView.as_view(), name='one_user'),
    path('user/<int:pk>/update', UsersPhoneUpdateView.as_view(), name='user_update'),
    path('api/users', users_list, name='users_list'),
    path('api/user/<int:pk>', user_detail, name='user_detail'),
]