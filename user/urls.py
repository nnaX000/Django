from django.urls import path
from .views import signup_view, login_view, password_search

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/',login_view,name='login'),
    path('password_search/',password_search,name='password_search')
]