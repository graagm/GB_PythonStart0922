from django.contrib import admin
from guides_phones.models import UsersPhone, Students
# Register your models here.


class UsersPhoneAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'phone_number', 'email')


admin.site.register(UsersPhone, UsersPhoneAdmin)


class StudentsAdmin(admin.ModelAdmin):
    list_display = ('user', 'corse', 'facultet', 'budjet')


admin.site.register(Students, StudentsAdmin)