from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
