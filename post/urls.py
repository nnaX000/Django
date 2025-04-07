from django.urls import path
from .views import post_create_view, post_detail_view, comment_create_view, comment_like_view, comment_reply_view, post_like_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('create/', post_create_view, name='post_create'),
    path('detail/<int:post_id>/', post_detail_view, name='post_detail'),
    path('<int:post_id>/comment/create/', comment_create_view, name='comment_create'),
    path('comment/<int:comment_id>/like/', comment_like_view, name='comment_like'),
    path('comment/<int:comment_id>/reply/', comment_reply_view, name='comment_reply'),
    path('post/<int:post_id>/like/', post_like_view, name='post_like'),
]

