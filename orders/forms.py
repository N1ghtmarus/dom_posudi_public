from django import forms

from .models import Order


class OrderCreateForm(forms.ModelForm):
    """ Форма данных о заказе """
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'pickup_point']
