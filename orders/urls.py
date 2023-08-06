from .orders import orders_index, download_factor
from django.urls import path


urlpatterns = [
    path("", orders_index, name = "orders"),
]