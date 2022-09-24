from .models import UsersPhone
from django.forms import ModelForm


class UsersPhoneForm(ModelForm):

    class Meta:
        model = UsersPhone
        fields = ('user_name', 'phone_number', 'email')