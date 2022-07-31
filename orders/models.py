from django.db import models

from shop.models import Product


PICKUP_POINT_CHOICES = (
    ("​Гагарина, 10", "​Гагарина, 10"),
    ("​​Карла Маркса, 153, ТРК Гостиный двор​",
    "​Карла Маркса, 153, ТРК Гостиный двор​"),
)


class Order(models.Model):
    """ Информация о заказчике и заказе """
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    email = models.EmailField('E-mail')
    pickup_point = models.CharField(
                                    'Пункт выдачи',
                                    max_length=200,
                                    choices=PICKUP_POINT_CHOICES
                                    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """ Информация о заказанном продукте"""
    order = models.ForeignKey(
                            Order,
                            related_name='items',
                            on_delete=models.CASCADE
                            )
    product = models.ForeignKey(
                                Product,
                                related_name='order_items',
                                on_delete=models.CASCADE
                                )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
