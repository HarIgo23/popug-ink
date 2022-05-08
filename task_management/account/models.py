from django.contrib.auth.models import AbstractUser
from django.db import models


class SystemRoles(models.TextChoices):
    ADMIN = 'admin'
    MANAGER = 'manager'
    WORKER = 'worker'


class Account(AbstractUser):
    system_role = models.CharField(max_length=12, choices=SystemRoles.choices, default=SystemRoles.WORKER)
