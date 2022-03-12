from django.urls import path

from board.views import BoardCreateView

urlpatterns = [
    path('create/', BoardCreateView.as_view())
]
