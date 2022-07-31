from django.contrib import admin

from .models import Category, Maker, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Maker)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['company', 'country', 'slug']
    prepopulated_fields = {'slug': ('company',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'maker', 'price',
    'available', 'sale', 'on_sale', 'created', 'updated']
    list_filter = ['available', 'on_sale', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
