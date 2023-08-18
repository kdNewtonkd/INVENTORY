from django.db import models
from django.contrib.auth.models import User
# Create your models here.

CATEGORY=(
    ('Stationary','stationary'),
    ('Electronics','Electronics'),
    ('Food','food')
)
class Product(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(max_length=100, choices=CATEGORY)
    quantity=models.PositiveIntegerField(null=True)

    class Meta:
        verbose_name_plural ='Product'

    def __str__(self):
        return f'{self.name}-{self.quantity}'


class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    staff=models.ForeignKey(User,models.CASCADE,null=True)
    order_quantity=models.PositiveBigIntegerField(null=True)
    date=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural ='Order'

    def __str__(self):
        return f'{self.product} ordered by {self.staff.username}'
