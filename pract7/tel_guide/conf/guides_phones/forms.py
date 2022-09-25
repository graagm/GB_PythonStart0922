from .models import UsersPhone, Students
from django.forms import ModelForm


class UsersPhoneForm(ModelForm):

    class Meta:
        model = UsersPhone
        fields = ('user_name', 'phone_number', 'email')


class StudentsForm(ModelForm):

    class Meta:
        model = Students
        fields = ('user', 'corse', 'facultet', 'budjet')