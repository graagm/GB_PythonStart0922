from django.contrib import admin
from guides_phones.models import UsersPhone
# Register your models here.


class UsersPhoneAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'phone_number', 'email')


admin.site.register(UsersPhone, UsersPhoneAdmin)