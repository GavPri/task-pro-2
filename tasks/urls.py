from . import views
from django.urls import path
from .views import AddTaskView


urlpatterns = [
    path('', views.TaskListView.as_view(), name='home'),
    path('add/', AddTaskView.as_view(), name='add_task'),
]
