from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from shop.models import Product
from coupons.models import Coupon
from decimal import Decimal

class Status(models.Model):
    status = models.CharField('Estdo de las orden',max_length=40, null = False, blank = False)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):
        return self.status


class Order(models.Model):
    first_name = models.CharField('Nombres',max_length=50, null = False, blank = False)
    last_name = models.CharField('Apellidos',max_length=50, null = False, blank = False)
    email = models.EmailField('Correo electronico',null = False, blank = False)
    address = models.CharField('Direccion',max_length=250,null = False, blank = False)
    postal_code = models.CharField('Codigo postal',max_length=20, null = False, blank = False)
    city = models.CharField('Cuidad',max_length=100,null = False, blank = False)
    created = models.DateTimeField(auto_now_add=True, null = False, blank = False)
    updated = models.DateTimeField(auto_now=True, null = False, blank = False)
    paid = models.ForeignKey(Status,default=1, on_delete = models.CASCADE, verbose_name="Estdo de pedido")
    coupon = models.ForeignKey(Coupon,
        related_name='orders', on_delete = models.CASCADE,
        null = True,
        blank = True)
    discount = models.IntegerField(default=0,
        validators = [MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_subtotal(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal('100'))

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete = models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
