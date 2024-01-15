# urls.py in time_management_app

from django.urls import path
from .views import home, user_login, user_signup, user_logout, task_list, add_task, previous_week, next_week

urlpatterns = [
    path('', home, name='home'),
    path('login/', user_login, name='user_login'),
    path('signup/', user_signup, name='user_signup'),
    path('logout/', user_logout, name='user_logout'),
    path('tasks/', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('previous-week/', previous_week, name='previous_week'),
    path('next-week/', next_week, name='next_week'),
]
