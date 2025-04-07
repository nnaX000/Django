from django.urls import path
from .views import post_create_view, post_detail_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('create/', post_create_view, name='post_create'),
    path('detail/<int:post_id>/', post_detail_view, name='post_detail') 
]

