from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField(name="login", max_length=32)
    password = models.CharField(max_length=32)

    def __str__(self):
        return "User by login: " + self.login