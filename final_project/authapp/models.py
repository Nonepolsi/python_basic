from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models

from quizapp.models import User



class CustomUser(AbstractUser):

    username_validator = ASCIIUsernameValidator()
    #quiz_user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True, blank=True)