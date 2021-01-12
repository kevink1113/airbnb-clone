from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# Register your models here.

# admin.py에서 Model을 가져오려면 register를 해야 한다.
# models.User를 CustomUser에 사용하고자 한다.
# == admin.site.register(models.User, CustomUserAdmin)

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar", "gender", "bio", "birthdate", "language", "currency", "superhost"
                )
            }
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username", "first_name", "email", "is_active", "language", "currency", "superhost", "is_staff", "is_superuser",
    )


