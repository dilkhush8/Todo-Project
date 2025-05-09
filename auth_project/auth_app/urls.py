from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    # path('dashboard/', views.dashboard_view, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),

    path('', views.todo_list, name='todo_list'),
    path('complete/<int:todo_id>', views.complete_todo, name='complete_todo'),
    path('delete/<int:todo_id>', views.delete_todo, name='delete_todo'),
    path('create/', views.create_todo, name='create_todo'),
    path('edit/<int:todo_id>/', views.edit_todo, name='edit_todo'),  # New URL for editing todos
]