from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('update/<str:pk>/', views.update_task, name='update_task'),
    path('delete/<str:pk>/', views.deleteTask, name='deleteTask'),
]