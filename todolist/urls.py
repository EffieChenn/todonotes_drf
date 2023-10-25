from django.urls import path
from .views import TaskListView

urlpatterns = [
    path('', TaskListView.as_view({'get': 'list', 'post': 'create'})),
    path('/<str:pk>', TaskListView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

]

