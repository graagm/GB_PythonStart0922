from django.urls import path
from .views import HeadMain, UsersPhoneCreateView, UsersPhoneListView, \
                    UsersPhoneDetailView, UsersPhoneUpdateView,\
                    users_list, user_detail, StudentsCreateView, \
                    StudentsListView, StudentDetailView, StudentUpdateView, \
                    students_list, student_detail



urlpatterns = [
    path('', HeadMain, name='Head'),
    path('add', UsersPhoneCreateView.as_view(), name='add_user'),
    path('all', UsersPhoneListView.as_view(), name='all_users'),
    path('user/<int:pk>', UsersPhoneDetailView.as_view(), name='one_user'),
    path('user/<int:pk>/update', UsersPhoneUpdateView.as_view(), name='user_update'),
    path('api/users', users_list, name='users_list'),
    path('api/user/<int:pk>', user_detail, name='user_detail'),
    path('students/add', StudentsCreateView.as_view(), name='add_student'),
    path('students/all', StudentsListView.as_view(), name='all_students'),
    path('students/<int:pk>', StudentDetailView.as_view(), name='one_student'),
    path('students/<int:pk>/update', StudentUpdateView.as_view(), name='student_update'),
    path('api/students', students_list, name='students_list'),
    path('api/student/<int:pk>', student_detail, name='student_detail'),
]