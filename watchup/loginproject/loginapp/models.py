from django.contrib.auth.models import User
from django.db import models

class user(models.Model):
    name = models.CharField('User_name',max_length=20)
    password = models.CharField('password',max_legth=20)
