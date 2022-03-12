from django.urls import path

from board.views import BoardCreateView, BoardDetailView, BoardListView

urlpatterns = [
    path('create/', BoardCreateView.as_view()),
    path('list/', BoardListView.as_view()),
    path('detail/<int:pk>/', BoardDetailView.as_view())
]
