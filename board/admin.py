from django.contrib import admin

from board.models import Board


class BoardAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "insert_user", "insert_date", "update_date")


admin.site.register(Board, BoardAdmin)
