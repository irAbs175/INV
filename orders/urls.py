from .orders import orders_index
from django.urls import path


urlpatterns = [
    path("", orders_index, name = "orders"),
]