from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import GuestBookEntry
from .forms import GuestBookForm
from user.models import CustomUser

@login_required
def guestbook_write_view(request, user_id):
    owner = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = GuestBookForm(request.POST)
        if form.is_valid():
            guestbook = form.save(commit=False)
            guestbook.owner = owner
            guestbook.writer = request.user
            guestbook.save()
            return redirect('guestbook_view', user_id=owner.id)
    else:
        form = GuestBookForm()
    return render(request, 'write.html', {'form': form, 'owner': owner})

