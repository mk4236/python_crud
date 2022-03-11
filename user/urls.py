from django.urls import path

from user import views

urlpatterns = [
    path('detail/', views.detail),
    path('create/', views.create),
    path('update/', views.update),
    path('login/', views.login),
    path('logout/', views.logout)
]
