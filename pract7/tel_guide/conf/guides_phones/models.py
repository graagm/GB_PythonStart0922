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


class Students(models.Model):

    class Course(models.TextChoices):
        первый = 'fi'
        второй = 'sc'
        третий = 'tr'
        четвертый = 'fo'
        пятый = 'fv'

    class Facultet(models.TextChoices):
        математика = 'ma'
        литература = 'li'
        история = 'hi'
        философия = 'ph'
        лингвистика = 'la'

    user = models.OneToOneField(UsersPhone, verbose_name='студент', on_delete=models.PROTECT, related_name='student_name')
    corse = models.CharField(max_length=2, null=False, blank=False, choices=Course.choices, default='fi', verbose_name='курс студента')
    facultet = models.CharField(max_length=2, null=False, blank=False, choices=Facultet.choices, default='fi', verbose_name='факультет')
    budjet = models.BooleanField(default=False, verbose_name='бюджетник?')
    
    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'список студентов'

    def __str__(self):
        return self.user
