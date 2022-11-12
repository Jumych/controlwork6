from django.db import models

STATUS_CHOICES = [("active", "Активно"), ("blocked", "Заблокировано")]
# Create your models here.

class Book_Guest(models.Model):
    name = models.CharField(max_length=60, null=False, blank=False, verbose_name='Имя Автора')
    email = models.EmailField(max_length=60, null=False, blank=False, verbose_name='Почта')
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    deadline = models.DateField(null=True, blank=True, verbose_name='Дата Выполнения')
    edit_time = models.DateField(null=True, blank=True, verbose_name='Время Изменения')
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=STATUS_CHOICES, verbose_name='Статус')

    def __str__(self):
        return f'{self.id}. {self.name}'
