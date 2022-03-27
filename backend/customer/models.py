from django.db import models


class Customer(models.Model):
    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    #user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Имя пользователя')
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name='Email')
    device = models.CharField(max_length=200, null=True, blank=True, verbose_name='ID устройства')

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.device
