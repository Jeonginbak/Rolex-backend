from django.db import models
from product.models import Product

class User(models.Model):
    name          = models.CharField(max_length=50)
    password      = models.CharField(max_length=200)
    liked_product = models.ManyToManyField(Product, through='Like')

    class Meta:
        db_table = 'users'

class Like(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    user    = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'likes'
