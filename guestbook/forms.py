from django import forms
from .models import GuestBookEntry

class GuestBookForm(forms.ModelForm):
    class Meta:
        model = GuestBookEntry
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': '방명록 내용을 입력하세요'}),
        }