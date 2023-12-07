from django.db import models
from django.contrib.auth.models import AbstractUser

from .validators import validate_image
from .services import upload_avatar_path


class CustomUser(AbstractUser):
    """ Custom user model """

    phone = models.CharField(max_length=13, blank=True)
    first_login = models.DateField(blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(
        upload_to=upload_avatar_path, 
        validators=[validate_image], 
        blank=True, null=True
    )
    is_deleted = models.BooleanField(default=False)

    REQUIRED_FIELDS = []
