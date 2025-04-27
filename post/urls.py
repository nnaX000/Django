from django.urls import path
from .views import post_create_view, post_detail_view, comment_create_view, comment_like_view, comment_reply_view, post_like_view, post_search_view, post_board_view

urlpatterns = [
    path('create/', post_create_view, name='post_create'),
    path('detail/<int:post_id>/', post_detail_view, name='post_detail'),
    path('<int:post_id>/comment/create/', comment_create_view, name='comment_create'),
    path('comment/<int:comment_id>/like/', comment_like_view, name='comment_like'),
    path('comment/<int:comment_id>/reply/', comment_reply_view, name='comment_reply'),
    path('post/<int:post_id>/like/', post_like_view, name='post_like'),
    path('search/',post_search_view,name='post_search'),
    path('board/', post_board_view, name='post_board')
]

