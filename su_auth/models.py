from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class ExtendUser(AbstractUser):
    email = models.EmailField(("email"), max_length=254)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    