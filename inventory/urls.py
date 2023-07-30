from .views import (inventory, products, add_products, materials, add_materials,
    add_products_cardex, add_materials_cardex, ProductsViewSet, MaterialsViewSet,
    ProductsCardexViewSet, MaterialsCardexsViewSet, product_cardex_export_to_excel,
    material_cardex_export_to_excel, product_cardex_export_to_pdf, material_cardex_export_to_pdf)
from .export import (product_list_export_to_excel, material_list_export_to_excel,
    product_list_pdf, material_list_pdf)
from .json import (js_add_products, js_update_products, js_add_materials, js_update_materials,)
from django.urls import path
from .additions import (add_broken_products_view, add_broken_materials_view, add_returned_products_view,
    add_returned_materials_view, broken_products_list, broken_materials_list, returned_products_list,
    returned_materials_list, js_add_broken_products, js_add_broken_materials, js_add_returned_products,
    js_add_returned_materials, broken_products_list_excel_export, broken_materials_list_excel_export,
    returned_products_list_excel_export, returned_materials_list_excel_export, broken_products_list_pdf_export,
    broken_materials_list_pdf_export, returned_products_list_pdf_export, returned_materials_list_pdf_export)


urlpatterns = [
    path("material_cardex_excel/<location__code__color>", material_cardex_export_to_excel, name = "material_cardex_excel"),
    path("product_cardex_excel/<location__code__color>", product_cardex_export_to_excel, name = "product_cardex_excel"),
    path("excel_returned_materials_list", returned_materials_list_excel_export, name = "excel_returned_materials_list"),
    path("material_cardex_pdf/<location__code__color>", material_cardex_export_to_pdf, name = "material_cardex_pdf"),
    path("excel_returned_products_list", returned_products_list_excel_export, name = "excel_returned_products_list"),
    path("pdf_returned_materials_list", returned_materials_list_pdf_export, name = "pdf_returned_materials_list"),
    path("excel_broken_materials_list", broken_materials_list_excel_export, name = "excel_broken_materials_list"),
    path("product_cardex_pdf/<location__code__color>", product_cardex_export_to_pdf, name = "product_cardex_pdf"),
    path("pdf_returned_products_list", returned_products_list_pdf_export, name = "pdf_returned_products_list"),
    path("excel_broken_products_list", broken_products_list_excel_export, name = "excel_broken_products_list"),
    path("pdf_broken_materials_list", broken_materials_list_pdf_export, name = "pdf_broken_materials_list"),
    path("pdf_broken_products_list", broken_products_list_pdf_export, name = "pdf_broken_products_list"),
    path("js_add_returned_materials", js_add_returned_materials, name = "js_add_returned_materials"),
    path('api/materials_cardex', MaterialsCardexsViewSet.as_view(), name = 'materials_cardex_api'),
    path("js_add_returned_products", js_add_returned_products, name = "js_add_returned_products"),
    path("add_returned_materials", add_returned_materials_view, name = "add_returned_materials"),
    path("materials/<location__code__color>", add_materials_cardex, name = "materials_cardex"),
    path('api/products_cardex', ProductsCardexViewSet.as_view(), name = 'products_cardex_api'),
    path("material_list_excel/", material_list_export_to_excel, name = "material_list_excel"),
    path("add_returned_products", add_returned_products_view, name = "add_returned_products"),
    path("js_dd_broken_materials", js_add_broken_materials, name = "js_dd_broken_materials"),
    path("products/<location__code__color>", add_products_cardex, name = "products_cardex"),
    path("js_add_broken_products", js_add_broken_products, name = "js_add_broken_products"),
    path("product_list_excel/", product_list_export_to_excel, name = "product_list_excel"),
    path("add_broken_materials", add_broken_materials_view, name = "add_broken_materials"),
    path("add_broken_products", add_broken_products_view, name = "add_broken_products"),
    path("returned_materials", returned_materials_list, name = "returned_materials"),
    path("js_update_materials", js_update_materials, name = "js_update_materials"),
    path("returned_products", returned_products_list, name = "returned_products"),
    path("js_update_products", js_update_products, name = "js_update_products"),
    path("broken_materials", broken_materials_list, name = "broken_materials"),
    path('api/materials', MaterialsViewSet.as_view(), name = 'materials_api'),
    path("broken_products", broken_products_list, name = "broken_products"),
    path('api/products', ProductsViewSet.as_view(), name = 'products-api'),
    path("js_add_materials", js_add_materials, name = "js_add_materials"),
    path("material_list_pdf", material_list_pdf, name = "Materials_list"),
    path("product_list_pdf", product_list_pdf, name = "products_list"),
    path("js_add_products", js_add_products, name = "js_add_products"),
    path("add_materials/", add_materials, name = "add_materials"),
    path("add_products/", add_products, name = "add_products"),
    path("materials/", materials, name = "materials"),
    path("products/", products, name = "products"),


    path("", inventory, name = "inventory")
]