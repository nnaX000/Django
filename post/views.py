from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Stack, PostImage

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


def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    images = post.images.all()
    return render(request, 'post_detail.html', {'post': post, 'images': images})

