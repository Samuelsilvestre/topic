from django.urls import path
from django.contrib.auth import views as auth_view

from .views import *

urlpatterns = [
    path('', HomeTemplateView.as_view(), name = 'home'),
    path('create/form/topic', TopicCreateView.as_view(), name = 'create_topic'),
    path('list/topic/', TopicListView.as_view(), name = 'list_topic'),
    path('login/user/', auth_view.LoginView.as_view(
        template_name='core/registro/login.html'
    ), name = 'login'),
    path('logout/user/', auth_view.LogoutView.as_view(), name = 'logout')
]