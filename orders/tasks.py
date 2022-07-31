from celery import shared_task
from django.core.mail import send_mail

from .models import Order


@shared_task
def send_email_task(order_id):
    """
    Таск, отправляющий оповещение на e-mail,
    когда заказ успешно создан
    """
    order = Order.objects.get(id=order_id)
    subject = f'Заказ номер {order.id}'
    message = f'{order.first_name},\n\n' \
        f'Ваш заказ успешно создан' \
        f'Номер вашего заказа {order.id}.'
    mail_sent = send_mail(
                        subject,
                        message,
                        'domposuditest@gmail.com',
                        [order.email]
                        )
    return mail_sent
