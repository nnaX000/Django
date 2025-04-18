from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Stack, PostImage, Comment
from django.contrib.auth.decorators import login_required

#글 작성하기
def post_create_view(request):
    if request.method == 'POST':
         title=request.POST['title']
         content=request.POST['content']
         github=request.POST['github']
         author=request.user

         post = Post.objects.create(
              title=title,
              content=content,
              github=github,
              author=author,
              view=1,
              likes=0
         )

         stack_ids = request.POST.getlist('stacks[]')
         post.stacks.set(stack_ids)

         images = request.FILES.getlist('images[]')
         for image in images:
            PostImage.objects.create(post=post, image=image)

         return redirect('post_detail', post_id=post.id)

    
    stacks=Stack.objects.all()
    return render(request, 'post_create.html',{'stacks':stacks})

#이미 작성한 글 보기
def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    images = post.images.all()
    return render(request, 'post_detail.html', {'post': post, 'images': images})

#댓글 작성
@login_required
def comment_create_view(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        content = request.POST.get('content')

        if content:
            Comment.objects.create(
                post=post,
                author=request.user,
                content=content,
                parent=None
            )

    return redirect('post_detail', post_id=post.id)

#댓글 좋아요
@login_required
def comment_like_view(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    user = request.user

    if user in comment.likes.all():
        comment.likes.remove(user) 
    else:
        comment.likes.add(user)

    return redirect('post_detail', post_id=comment.post.id)

#대댓글 좋아요
@login_required
def comment_reply_view(request, comment_id):
    parent_comment = get_object_or_404(Comment, id=comment_id)

    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            Comment.objects.create(
                post=parent_comment.post,
                author=request.user,
                content=content,
                parent=parent_comment 
            )

    return redirect('post_detail', post_id=parent_comment.post.id)

#게시물 좋아요
@login_required
def post_like_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)

    return redirect('post_detail', post_id=post.id)