from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Order


@shared_task
def order_created(order_id):
    """
    Task for send notification by email to user when order was created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order_id}'
    message = (
        f'Dear {order.first_name},\n\n'
        f'You have successfully placed an order.'
        f'Your order ID is {order.id}.'
    )
    mail_sent = send_mail(subject, message, settings.ADMIN_EMAIL, [order.email])
    return mail_sent
