'''Model'''
#from re import I
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
#from more_itertools import quantify
from django.db.models import Sum

# Create your models here.

class Category(models.Model):
    '''category'''
    name = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=2, choices=(('1', 'Active'), ('2', 'Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    '''Product'''
    code = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField()
    price = models.FloatField(default=0)
    status = models.CharField(max_length=2, choices=(('1', 'Active'), ('2', 'Inactive')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code + ' - ' + self.name

    def count_inventory(self):
        '''Inventory'''
        stocks = Stock.objects.filter(product=self)
        stock_in = 0
        stock_out = 0
        for stock in stocks:
            if stock.type == '1':
                stock_in = int(stock_in) + int(stock.quantity)
            else:
                stock_out = int(stock_out) + int(stock.quantity)
        available = stock_in - stock_out
        return available

class Stock(models.Model):
    '''Stock'''
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    type = models.CharField(max_length=2, choices=(('1', 'Stock-in'), ('2', 'Stock-Out')), default=1)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.code + ' - ' + self.product.name

class Invoice(models.Model):
    '''Invoice'''
    transaction = models.CharField(max_length=250)
    customer = models.CharField(max_length=250)
    total = models.FloatField(default=0)
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.transaction

    def item_count(self):
        '''category'''
        return Invoice_Item.objects.filter(invoice=self).aggregate(Sum('quantity'))['quantity__sum']

class Invoice_Item(models.Model):
    '''Invoice'''
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, blank=True, null=True)
    price = models.FloatField(default=0)
    quantity = models.FloatField(default=0)

    def __str__(self):
        return self.invoice.transaction


@receiver(models.signals.post_save, sender=Invoice_Item)
def stock_update(sender, instance, **kwargs):
    '''Stock'''
    print(sender)
    print(instance)
    print(kwargs)
    stock = Stock(product=instance.product, quantity=instance.quantity, type=2)
    stock.save()
    # stockID = Stock.objects.last().id
    Invoice_Item.objects.filter(id=instance.id).update(stock=stock)

@receiver(models.signals.post_delete, sender=Invoice_Item)
def delete_stock(sender, instance, **kwargs):
    '''delete_stock'''
    print(sender)
    print(instance)
    print(kwargs)
    try:
        stock = Stock.objects.get(id=instance.stock.id).delete()
    except Exception:
        return instance.stock.id
        