from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, FileResponse
from .models import (SiteOrders)
from django.conf import settings


@csrf_exempt
@login_required
def orders_index(request):
    if request.method == 'POST':
        job = request.POST.get('job')
        if job == 'submit_new_orders':
            order_code = request.POST.get('order_code')
            full_name = request.POST.get('full_name')
            phone_number = request.POST.get('phone_number')
            package_status = request.POST.get('package_status')
            send_method = request.POST.get('send_method')
            order_desc = request.POST.get('order_desc')
            if order_code != "":
                if full_name !="":
                    if phone_number != "":
                        if order_desc != "":
                            # get database
                            order = SiteOrders.objects.filter(
                                order_code = order_code,)
                            if package_status == "بسته بندی نشده":
                                order.update(
                                    submit_by = request.user.email,
                                    order_code = order_code,
                                    full_name = full_name,
                                    phone_number = phone_number,
                                    package_status = False,
                                    send_status = False,
                                    send_method = send_method,)
                                # Success message
                                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                                sended_orders = SiteOrders.objects.filter(send_status = True)
                                message = 'سفارش با موفقیت به روز رسانی شد'
                                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                                return render(request, "orders/orders_index.html", context = context)
                            elif package_status =="بسته بندی شده":
                                order.update(
                                    submit_by = request.user.email,
                                    order_code = order_code,
                                    full_name = full_name,
                                    phone_number = phone_number,
                                    package_status = True,
                                    send_status = False,
                                    send_method = send_method,)
                                # Success message
                                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                                sended_orders = SiteOrders.objects.filter(send_status = True)
                                message = 'سفارش با موفقیت به روز رسانی شد'
                                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                                return render(request, "orders/orders_index.html", context = context)
                            else:
                                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                                sended_orders = SiteOrders.objects.filter(send_status = True)
                                message = 'توضیحات سفارش خالیست'  
                                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                                return render(request, "orders/orders_index.html", context = context)
                        else:
                            new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                            packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                            sended_orders = SiteOrders.objects.filter(send_status = True)
                            message = 'توضیحات سفارش خالیست'  
                            context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                            return render(request, "orders/orders_index.html", context = context)
                    else:
                        new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                        packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                        sended_orders = SiteOrders.objects.filter(send_status = True)
                        message = 'شماره تلفن وارد نشده'  
                        context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                        return render(request, "orders/orders_index.html", context = context)
                else:
                    new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                    packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                    sended_orders = SiteOrders.objects.filter(send_status = True)
                    message = 'نام و نام خانوادگی وارد نشده'
                    context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                    return render(request, "orders/orders_index.html", context = context)
            else:
                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                sended_orders = SiteOrders.objects.filter(send_status = True)
                message = 'کد سفارش وارد نشده'
                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                return render(request, "orders/orders_index.html", context = context)
        elif job == 'submit_packaged_orders':
            order_code = request.POST.get('order_code')
            full_name = request.POST.get('full_name')
            phone_number = request.POST.get('phone_number')
            package_status = request.POST.get('package_status')
            send_status = request.POST.get('send_status')
            send_method = request.POST.get('send_method')
            order_desc = request.POST.get('order_desc')
            if order_code != "":
                if full_name !="":
                    if phone_number != "":
                        if order_desc != "":
                            # get database
                            order = SiteOrders.objects.filter(
                                order_code = order_code,
                            )
                            if send_status == "پست نشده":
                                order.update(send_status = False, submit_by = request.user.email,)
                                # Success message
                                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                                sended_orders = SiteOrders.objects.filter(send_status = True)
                                message = 'سفارش با موفقیت به روز رسانی شد'
                                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                                return render(request, "orders/orders_index.html", context = context)
                            elif send_status == "پست شده":
                                order.update(send_status = True, submit_by = request.user.email,)
                                # Success message
                                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                                sended_orders = SiteOrders.objects.filter(send_status = True)
                                message = 'سفارش با موفقیت به روز رسانی شد'
                                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                                return render(request, "orders/orders_index.html", context = context)
                            else:
                                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                                sended_orders = SiteOrders.objects.filter(send_status = True)
                                message = 'شماره تلفن وارد نشده'  
                                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                                return render(request, "orders/orders_index.html", context = context)
                        else:
                            new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                            packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                            sended_orders = SiteOrders.objects.filter(send_status = True)
                            message = 'توضیحات سفارش خالیست'  
                            context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                            return render(request, "orders/orders_index.html", context = context)
                    else:
                        new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                        packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                        sended_orders = SiteOrders.objects.filter(send_status = True)
                        message = 'شماره تلفن وارد نشده'  
                        context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                        return render(request, "orders/orders_index.html", context = context)
                else:
                    new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                    packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                    sended_orders = SiteOrders.objects.filter(send_status = True)
                    message = 'نام و نام خانوادگی وارد نشده'
                    context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                    return render(request, "orders/orders_index.html", context = context)
            else:
                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                sended_orders = SiteOrders.objects.filter(send_status = True)
                message = 'کد سفارش وارد نشده'
                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                return render(request, "orders/orders_index.html", context = context)
        elif job == 'submit_sended_orders':
            order_code = request.POST.get('order_code')
            full_name = request.POST.get('full_name')
            phone_number = request.POST.get('phone_number')
            package_status = request.POST.get('package_status')
            send_status = request.POST.get('send_status')
            send_method = request.POST.get('send_method')
            order_desc = request.POST.get('order_desc')
            if order_code != "":
                if full_name !="":
                    if phone_number != "":
                        if order_desc != "":
                            # get database
                            order = SiteOrders.objects.filter(
                                order_code = order_code,
                            )
                            if send_status == "پست نشده":
                                order.update(send_status = False, submit_by = request.user.email,)
                                # Success message
                                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                                sended_orders = SiteOrders.objects.filter(send_status = True)
                                message = 'سفارش با موفقیت به روز رسانی شد'
                                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                                return render(request, "orders/orders_index.html", context = context)
                            elif send_status == "پست شده":
                                order.update(send_status = True, submit_by = request.user.email,)
                                # Success message
                                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                                sended_orders = SiteOrders.objects.filter(send_status = True)
                                message = 'سفارش با موفقیت به روز رسانی شد'
                                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                                return render(request, "orders/orders_index.html", context = context)
                            else:
                                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                                sended_orders = SiteOrders.objects.filter(send_status = True)
                                message = 'شماره تلفن وارد نشده'  
                                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                                return render(request, "orders/orders_index.html", context = context)
                        else:
                            new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                            packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                            sended_orders = SiteOrders.objects.filter(send_status = True)
                            message = 'توضیحات سفارش خالیست'  
                            context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                            return render(request, "orders/orders_index.html", context = context)
                    else:
                        new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                        packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                        sended_orders = SiteOrders.objects.filter(send_status = True)
                        message = 'شماره تلفن وارد نشده'  
                        context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                        return render(request, "orders/orders_index.html", context = context)
                else:
                    new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                    packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                    sended_orders = SiteOrders.objects.filter(send_status = True)
                    message = 'نام و نام خانوادگی وارد نشده'
                    context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                    return render(request, "orders/orders_index.html", context = context)
            else:
                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                sended_orders = SiteOrders.objects.filter(send_status = True)
                message = 'کد سفارش وارد نشده'
                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                return render(request, "orders/orders_index.html", context = context)
        elif job == 'submit_search':
            searched_text = request.POST.get('searched_text')
            if searched_text != "":
                order = SiteOrders.objects.filter(order_code__contains = searched_text)
                if order.exists():
                    search_result = SiteOrders.objects.filter(order_code__contains = searched_text)
                    new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                    packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                    sended_orders = SiteOrders.objects.filter(send_status = True)
                    message = ''
                    context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':search_result, 'message': message}
                    return render(request, "orders/orders_index.html", context = context)
                else:
                    new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                    packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                    sended_orders = SiteOrders.objects.filter(send_status = True)
                    message = 'کد سفارش جستجو شده یافت نشد'
                    context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                    return render(request, "orders/orders_index.html", context = context)
            else:
                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                sended_orders = SiteOrders.objects.filter(send_status = True)
                message = 'کد سفارشی جستجو نکردید !'
                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                return render(request, "orders/orders_index.html", context = context)
        elif job == 'edit_search':
            order_code = request.POST.get('order_code')
            full_name = request.POST.get('full_name')
            phone_number = request.POST.get('phone_number')
            package_status = request.POST.get('package_status')
            send_status = request.POST.get('send_status')
            send_method = request.POST.get('send_method')
            order_desc = request.POST.get('order_desc')
            if order_code != "":
                if full_name !="":
                    if phone_number != "":
                        if order_desc != "":
                            if package_status == "بسته بندی شده":
                                PACKAGE = True
                            elif package_status == "بسته بندی نشده":
                                PACKAGE = False
                            if send_status == "پست شده":
                                SEND = True
                            elif send_status == "پست نشده":
                                SEND = False
                            order = SiteOrders.objects.filter(order_code = order_code,)
                            order.update(
                                submit_by = request.user.email,
                                order_code = order_code,
                                full_name = full_name,
                                phone_number = phone_number,
                                package_status = PACKAGE,
                                send_status = SEND,
                                send_method = send_method,
                                order_desc = order_desc,)
                            new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                            packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                            sended_orders = SiteOrders.objects.filter(send_status = True)
                            message = 'سفارش با موفقیت به روز رسانی شد'
                            context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                            return render(request, "orders/orders_index.html", context = context)
                        else:
                            new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                            packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                            sended_orders = SiteOrders.objects.filter(send_status = True)
                            message = 'توضیحات سفارش خالیست'  
                            context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                            return render(request, "orders/orders_index.html", context = context)
                    else:
                        new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                        packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                        sended_orders = SiteOrders.objects.filter(send_status = True)
                        message = 'شماره تلفن وارد نشده'  
                        context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                        return render(request, "orders/orders_index.html", context = context)
                else:
                    new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                    packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                    sended_orders = SiteOrders.objects.filter(send_status = True)
                    message = 'نام و نام خانوادگی وارد نشده'
                    context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                    return render(request, "orders/orders_index.html", context = context)
            else:
                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                sended_orders = SiteOrders.objects.filter(send_status = True)
                message = 'کد سفارش وارد نشده'
                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                return render(request, "orders/orders_index.html", context = context)
        elif job == 'submit_order':
            order_code = request.POST.get('order_code')
            full_name = request.POST.get('full_name')
            phone_number = request.POST.get('phone_number')
            order_desc = request.POST.get('order_desc')
            if order_code != "":
                if full_name !="":
                    if phone_number != "":
                        if order_desc != "":
                            # get database
                            order = SiteOrders.objects.filter(order_code = order_code,)
                            if order.exists():
                                # order is exist error
                                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                                sended_orders = SiteOrders.objects.filter(send_status = True)
                                message = 'سفارش از پیش موجود است' 
                                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                                return render(request, "orders/orders_index.html", context = context)
                            else:
                                fs = FileSystemStorage()
                                uploaded_file = request.FILES['myfile']
                                filename = fs.save(uploaded_file.name, uploaded_file)
                                SiteOrders.objects.create(
                                order_code = order_code,
                                full_name = full_name,
                                phone_number = phone_number,
                                package_status = False,
                                send_status = False,
                                send_method = "روش ارسال انتخاب نشده",
                                factor_file = filename,
                                order_desc = order_desc,
                                )
                                # Success message
                                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                                sended_orders = SiteOrders.objects.filter(send_status = True)
                                message = 'سفارش با موقیت ایجاد شد'
                                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                                return render(request, "orders/orders_index.html", context = context)
                        else:
                            new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                            packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                            sended_orders = SiteOrders.objects.filter(send_status = True)
                            message = 'توضیحات سفارش خالیست'  
                            context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                            return render(request, "orders/orders_index.html", context = context)
                    else:
                        new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                        packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                        sended_orders = SiteOrders.objects.filter(send_status = True)
                        message = 'شماره تلفن وارد نشده'  
                        context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                        return render(request, "orders/orders_index.html", context = context)
                else:
                    new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                    packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                    sended_orders = SiteOrders.objects.filter(send_status = True)
                    message = 'نام و نام خانوادگی وارد نشده'
                    context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                    return render(request, "orders/orders_index.html", context = context)
            else:
                new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
                packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
                sended_orders = SiteOrders.objects.filter(send_status = True)
                message = 'کد سفارش وارد نشده'
                context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
                return render(request, "orders/orders_index.html", context = context)
    else:
        new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
        packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
        sended_orders = SiteOrders.objects.filter(send_status = True)
        message = ''
        context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
        return render(request, "orders/orders_index.html", context = context)
    new_orders = SiteOrders.objects.filter(send_status = False, package_status = False)
    packaged_orders = SiteOrders.objects.filter(package_status = True, send_status = False)
    sended_orders = SiteOrders.objects.filter(send_status = True)
    message = ''
    context = {'new_orders':new_orders,'packaged_orders':packaged_orders, 'sended_orders':sended_orders, 'search_result':'', 'message': message}
    return render(request, "orders/orders_index.html", context = context)

@csrf_exempt
@login_required
def download_factor(request, code):
    order = get_object_or_404(SiteOrders, order_code = code)
    upload_link = order.factor_file
    response = FileResponse(open(upload_link.path, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{upload_link.name}"'
    return response