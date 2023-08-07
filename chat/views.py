from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from account.models import user_accounts


@login_required
def pvmessage(request, room):
    account = user_accounts.objects.filter(last_name = room)
    if account.exists():
        return render(request, "chat/private.html", {"room_name": room})
    else:
        return render(request, "dashboard/dashboard.html")