from django.db import models
from user.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'

class Collection(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'collections'

class Product(models.Model):
    category          = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    collection        = models.ForeignKey('Collection', on_delete=models.SET_NULL, null=True)
    middle_image      = models.ForeignKey('MiddleImage', on_delete=models.SET_NULL, null=True)
    detail            = models.ForeignKey('Detail', on_delete=models.SET_NULL, null=True)
    header_watch      = models.URLField(max_length=1000)
    header_background = models.URLField(max_length=1000)
    description       = models.CharField(max_length=500)
    sub_description   = models.CharField(max_length=500)

    class Meta:
        db_table = 'products'

class MiddleImage(models.Model):
    thumbnail_url = models.URLField(max_length=1000)
    image_url     = models.URLField(max_length=1000)
    title         = models.CharField(max_length=50)
    sub_title     = models.CharField(max_length=50)
    description   = models.CharField(max_length=1000)

    class Meta:
        db_table = 'middle_images'

class Feature(models.Model):
    product       = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    title         = models.CharField(max_length=50)
    sub_title     = models.CharField(max_length=50)
    description   = models.CharField(max_length=500)
    thumbnail_url = models.URLField(max_length=1000)
    image_url     = models.URLField(max_length=1000)

    class Meta:
        db_table = 'features'

class Detail(models.Model):
    size      = models.ForeignKey('Size', on_delete=models.SET_NULL, null=True)
    material  = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True)
    bezel     = models.ForeignKey('Bezel', on_delete=models.SET_NULL, null=True)
    bracelet  = models.ForeignKey('Bracelet', on_delete=models.SET_NULL, null=True)
    dial      = models.ForeignKey('Dial', on_delete=models.SET_NULL, null=True)
    is_oyster = models.BooleanField()
    price     = models.IntegerField()

    class Meta:
        db_table = 'details' 

class ConfigureWatch(models.Model):
    user     = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    size     = models.ForeignKey('Size', on_delete=models.SET_NULL, null=True)
    material = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True)
    bezel    = models.ForeignKey('Bezel', on_delete=models.SET_NULL, null=True)
    bracelet = models.ForeignKey('Bracelet', on_delete=models.SET_NULL, null=True)
    dial     = models.ForeignKey('Dial', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'configure_watches'

class Size(models.Model):
    diameter = models.IntegerField()

    class Meta:
        db_table = 'sizes'

class Material(models.Model):
    name           = models.CharField(max_length=50)
    image_url      = models.URLField(max_length=1000)
    background_url = models.URLField(max_length=1000)

    class Meta:
        db_table = 'materials'

class Bezel(models.Model):
    name = models.CharField(max_length=50)   

    class Meta:
        db_table = 'bezels'      

class Bracelet(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'bracelets'

class Dial(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'dials'

class BezelFind(models.Model):
    size      = models.ForeignKey('Size', on_delete=models.SET_NULL, null=True)
    material  = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True)
    bezel     = models.ForeignKey('Bezel', on_delete=models.SET_NULL, null=True)
    image_url = models.URLField(max_length=1000)
    
    class Meta:
        db_table = 'bezels_finds'        

class BraceletFind(models.Model):
    size      = models.ForeignKey('Size', on_delete=models.SET_NULL, null=True)
    material  = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True)
    bezel     = models.ForeignKey('Bezel', on_delete=models.SET_NULL, null=True)
    bracelet  = models.ForeignKey('Bracelet', on_delete=models.SET_NULL, null=True)
    image_url = models.URLField(max_length=1000)
    
    class Meta:
        db_table = 'bracelets_finds'          

class DialFind(models.Model):
    size        = models.ForeignKey('Size', on_delete=models.SET_NULL, null=True)
    material    = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True)
    dial        = models.ForeignKey('Dial', on_delete=models.SET_NULL, null=True)
    image_url   = models.URLField(max_length=1000)
    
    class Meta:
        db_table = 'dials_finds'  
