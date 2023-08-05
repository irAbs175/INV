from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
#from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from .models import (SiteOrders)


@login_required
def orders_index(request):
    return render(request, "orders/orders_index.html")