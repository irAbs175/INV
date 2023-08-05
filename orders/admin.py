from django.contrib import admin
from .models import SiteOrders


class SiteOrdersAdmin(admin.ModelAdmin):
    list_display = ('order_code', 'full_name', 'phone_number', 'package_status', 'send_method', 'factor_file', 'order_time')
    list_filter = ('order_code', 'full_name', 'phone_number', 'package_status', 'send_method', 'factor_file', 'order_time')
    search_fields = ('order_code', 'full_name', 'phone_number', 'package_status', 'send_method', 'factor_file', 'order_time')


admin.site.register(SiteOrders, SiteOrdersAdmin)