from django.shortcuts import render
import logging

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import send_email_task


logger = logging.getLogger(__name__)


def order_create(request):
    """
    Веб-сервис, сохраняющий данные о заказе,
    добавляющий все товары из корзины в базу данных
    и запускающий таск отправки сообщений на e-mail
    """
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                                        order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantity']
                                        )

            # отчищаем корзину
            cart.clear()
            # запускаем celery таск
            try:
                send_email_task.delay(order.id)
            except Exception as e:
                logger.error(e)

            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
