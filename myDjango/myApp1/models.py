from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Worker(models.Model):
    name = models.CharField(max_length=10, blank=False)
    surname = models.CharField(max_length=20)
    salary = models.IntegerField(default=0)

    # def __str__(self):
    #     return f'{self.name} {self.surname} {self.salary}'
