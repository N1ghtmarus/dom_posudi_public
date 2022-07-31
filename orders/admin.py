from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'pickup_point',
        'paid',
        'created',
        'updated',
        ]
    list_filter = [
        'paid',
        'pickup_point',
        'created',
        'updated',
        ]
    inlines = [OrderItemInline]
