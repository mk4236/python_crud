from django.contrib import admin

from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "user_name", "user_email", "insert_date")


admin.site.register(User, UserAdmin)
