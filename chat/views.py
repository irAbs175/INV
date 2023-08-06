from django.shortcuts import render


def pvmessage(request, room):
    return render(request, "chat/public.html", {"room_name": "TST"})