from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class UsersPhone(models.Model):
    user_name = models.CharField(max_length=20, unique=True, verbose_name='Имя', help_text="введите Ваш ник")
    phone_number = PhoneNumberField(unique=True, null = False, verbose_name="номер", help_text="Такой формат +79611234567")
    email = models.EmailField(max_length=30, null = False, verbose_name = "адрес эл почты")
    
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'телефоны'

    def __str__(self):
        return self.user_name
