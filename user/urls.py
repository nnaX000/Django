from django.urls import path
from .views import signup_view, login_view, password_search, mypage_view, edit_profile_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/',login_view,name='login'),
    path('password_search/',password_search,name='password_search'),
    path('password_email/', auth_views.PasswordResetView.as_view(template_name='user/registration/password_reset_form.html'),name='password_email'), 
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('my_page/', mypage_view, name='mypage'),
    path('mypage/edit/', edit_profile_view, name='edit_profile'),
]