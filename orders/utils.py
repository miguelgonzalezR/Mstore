from django.core.mail import send_mail
from .models import Order
from .models import OrderItem
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string

def order_created(order_id):
    order = Order.objects.get(id=order_id)
    dorder = OrderItem.objects.filter(order = order_id)
    subject = 'Numero del pedido: {}'.format(order.id)
    message = 'Cliente: {}, \n\nSu pedido se a creado con exito.El numero de su pedido es: {}, Su total es de {}$ . \n\n{}.'.format(order.first_name, order.id, order.get_total_cost(), render_to_string("orders/order/depe.html",{'det':dorder}))
    html_body = render_to_string("orders/order/depe.html")

    mail_sent = send_mail(subject, message, 'miguelgr1019@gmail.com', [order.email])

    return mail_sent
