from django.urls import path
from .views import pvmessage


urlpatterns = [
    path("<room>", pvmessage),
]
