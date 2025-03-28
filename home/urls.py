from django.urls import path
from .views import home_view,logout_view

urlpatterns = [
    #홈 화면으로 렌더링되는 url
    path('', home_view, name='home'),

    #로그아웃 url
    path('logout/', logout_view, name="logout")
]