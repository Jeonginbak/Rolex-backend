from django.db import models

class User(models.Model):
    name          = models.CharField(max_length=50)
    password      = models.CharField(max_length=200)
    liked_product = models.ManyToManyField('product.Product', through='Like')
    size          = models.ManyToManyField('product.Size', through='product.ConfigureWatch')
    material      = models.ManyToManyField('product.Material', through='product.ConfigureWatch')
    bezel         = models.ManyToManyField('product.Bezel', through='product.ConfigureWatch')
    bracelet      = models.ManyToManyField('product.Bracelet', through='product.ConfigureWatch')
    dial          = models.ManyToManyField('product.Dial', through='product.ConfigureWatch')

    class Meta:
        db_table = 'users'

class Like(models.Model):
    product = models.ForeignKey('product.Product', on_delete=models.SET_NULL, null=True)
    user    = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'likes'
