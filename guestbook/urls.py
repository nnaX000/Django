from django.urls import path
from .views import guestbook_write_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('<str:user_id>/write/', guestbook_write_view, name='guestbook_write'),
]