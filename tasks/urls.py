from django.urls import path
from .views import TaskApi

urlpatterns = [
  path('list', TaskApi.as_view({'get': 'tasks_list'}),name="testList"),
  path('finished', TaskApi.as_view({'get': 'tasks_finished_list'}),name="finishedTasks"),
  path('unfinished', TaskApi.as_view({'get': 'tasks_unfinished_list'}),name="unfinishedTasks"),
  path('mark_as_complete/<int:task_id>', TaskApi.as_view({'get': 'mark_task_as_complete'}),name="markAsCompleteTask"),
]