from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.OneToOneField(User, max_length=50, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, verbose_name="User bio")

    def __str__(self):
        return str(self.name)