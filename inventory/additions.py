''' inventory additions (returned-broken products/materials) '''

from .models import (Products, Materials, ProductsCardex, MaterialsCardex)
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render


# ADD BROKEN-RETURNED PRODUCTS/MATERIALS PAGE VIEWS
''' The following function return view of broken products html view '''
@login_required
def add_broken_products_view(request):
    pass

''' The following function return view of broken materials html view '''
@login_required
def add_broken_materials_view(request):
    pass

''' The following function return view of returned products html view '''
@login_required
def add_returned_products_view(request):
    pass

''' The following function return view of returned materials html view '''
@login_required
def add_returned_materials_view(request):
    pass

# LIST OF BROKEN-RETURNED PRODUCTS/MATERIALS
''' The following function return broken products archive '''
@login_required
def broken_products_list()
pass

''' The following function return broken materials archive '''
@login_required
def broken_materials_list()
pass

''' The following function return returned products archive '''
@login_required
def returned_products_list()
pass

''' The following function return returned materials archive '''
@login_required
def returned_materials_list()
pass

# REST SUBMIT NEW BROKEN-RETURNED PRODUCTS/MATERIALS
''' The following function submit new broken products '''
@login_required
def js_add_broken_products(request):
    pass

''' The following function submit new broken materials '''
@login_required
def js_add_broken_materials(request):
    pass

''' The following function submit new returned products '''
@login_required
def js_add_returned_products(request):
    pass
    
''' The following function submit new returned materials '''
@login_required
def js_add_returned_materials(request):
    pass

# EXCEL EXPORT LIST OF BROKEN-RETURNED PRODUCTS/MATERIALS
''' The following function return excel export for broken products list '''
@login_required
def broken_products_list_excel_export(request):
    pass

''' The following function return excel export for broken materials list '''
@login_required
def broken_materials_list_excel_export(request):
    pass

''' The following function return excel export for returned products list '''
@login_required
def returned_products_list_excel_export(request):
    pass

''' The following function return excel export for returned materials list '''
@login_required
def returned_materials_list_excel_export(request):
    pass

# PDF EXPORT LIST OF BROKEN-RETURNED PRODUCTS/MATERIALS
''' The following function return pdf export for broken products list '''
@login_required
def broken_products_list_pdf_export(request):
    pass

''' The following function return pdf export for broken materials list '''
@login_required
def broken_materials_list_pdf_export(request):
    pass

''' The following function return pdf export for returned products list '''
@login_required
def returned_products_list_pdf_export(request):
    pass

''' The following function return pdf export for returned materials list '''
@login_required
def returned_materials_list_pdf_export(request):
    pass