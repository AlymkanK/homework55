from django.db import models

# Create your models here.
status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'),  ('done', 'Сделано')]

class Task(models.Model):
    description = models.CharField(max_length=150, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=20, null=False, blank=False, verbose_name="Статус", choices=status_choices, default='new')
    date = models.DateField(verbose_name= 'Дата')


    def __str__(self):
        return f"{self.description}, {self.status}, {self.date}"


    class Meta:
        db_table = 'Tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'