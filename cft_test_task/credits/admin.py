from django.contrib import admin
from .models import Manufacturer, Product, Contract, CreditApplication


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",)
    ordering = ("id",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "manufacturer", "created_at")
    list_filter = ("manufacturer",)
    search_fields = ("name",)
    ordering = ("id",)


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "number", "created_at")
    search_fields = ("number",)
    ordering = ("id",)


@admin.register(CreditApplication)
class CreditApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "contract", "created_at")
    search_fields = ("contract__number",)
    ordering = ("id",)
