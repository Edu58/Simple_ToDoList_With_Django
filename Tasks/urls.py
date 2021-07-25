from django.urls import path
from .views import Taskslist
from .views import CreateTask, Taskdetail, UpdateTask, DeleteTask

urlpatterns = [
    path('', Taskslist.as_view(), name ='tasks'),
    path('addtask/', CreateTask.as_view(), name='addtask'),
    path('taskdetail/<int:pk>/', Taskdetail.as_view(), name="task_detail"),
    path('updatetask/<int:pk>', UpdateTask.as_view(), name= "update_task"),
    path('deletetask/<int:pk>', DeleteTask.as_view(), name='delete_task'),
]
