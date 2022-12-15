from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('taskupdate/<str:pk>/', views.updateTask, name='taskupdate'),
    path('deletetask/<str:pk>/', views.deleteTask, name='taskdelete'),
]