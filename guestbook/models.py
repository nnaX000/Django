from django.db import models
from django.conf import settings

class GuestBookEntry(models.Model):
    owner = models.ForeignKey(  # 방명록 주인
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='guestbook_entries'
    )
    writer = models.ForeignKey(  # 글쓴이
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='written_guestbooks'
    )
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.writer} → {self.owner}: {self.content[:20]}'
