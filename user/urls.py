from django.urls import path

from user import views

urlpatterns = [
    path('detail/', views.detail),
    path('create/', views.create),
    path('login/', views.login),
    path('logout/', views.logout)
]
