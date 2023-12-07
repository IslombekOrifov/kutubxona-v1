from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin): 
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "middle_name", "email")}),
        (("Permissions"),{"fields": ("is_active", "is_staff", "is_superuser", "is_deleted", "groups", "user_permissions",),},),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
        (("Custom info"), {"fields": ("phone", "avatar")}),
    )
