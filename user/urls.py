from django.urls import path

from user import views

urlpatterns = [
    path('create/', views.create)
]
