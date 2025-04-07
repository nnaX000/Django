from django.db import models
from django.conf import settings

#스택 카테고리(여기에 스택 정보를 넣고 불러다 씀)
class Stack(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#게시물 테이블
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True, null=False)
    content=models.CharField(max_length=1000, blank=True, null=False)
    stacks = models.ManyToManyField(Stack, related_name="posts")
    github=models.CharField(max_length=100,blank=True, null=True)
    view = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#이미지는 post와 일대다 관계이므로 따로 테이블을 빼준다
class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/')