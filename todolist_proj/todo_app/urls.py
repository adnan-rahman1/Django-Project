from django.urls import path
from . import views


urlpatterns = [
    path('showtodos/', views.showTodos, name='showTodos'),
    path('addtodos/', views.addTodos, name='addTodos'),
    path('completeTodos/<int:task_id>', views.completeTodos, name='completeTodos'),
    path('deleteTodos/', views.deleteTodos, name='deleteTodos'),
    path('deleteAllTodos/', views.deleteAllTodos, name='deleteAllTodos'),
]



