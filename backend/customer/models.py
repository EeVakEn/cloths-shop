from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    class Meta:
        db_table = 'customer'
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    phone = models.CharField(max_length=10,
                             blank=True,
                             help_text="Номер телефона",
                             validators=[RegexValidator(
                                 regex=r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'
                             )], )
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    sreet = models.CharField(max_length=255, blank=True)
    house = models.CharField(max_length=255, blank=True)
    room = models.CharField(max_length=255, blank=True)
    zip = models.IntegerField(null=True,
                              blank=True,
                              help_text="Почтовый индекс",
                              validators=[RegexValidator(
                                  regex=r'^[0-9]{5,6}$',
                                  message='Формат почтового индекса: Россия, Белорусь - 123456, Украина - 12345'),
                              ], )

    def __str__(self):
        return self.user.username
