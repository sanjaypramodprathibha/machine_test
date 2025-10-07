from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:id>/', views.UserDetailView.as_view(), name='user-detail'),
]
