from django.db import models

# Create your models here.
class IceCream(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    class Meta:
        managed = False
        db_table = 'IceCream'

class Shop(models.Model):
    name=models.CharField(max_length=60)
    address=models.CharField(max_length=50)
    icecreamid=models.ForeignKey('IceCream',models.DO_NOTHING, db_column='ID',blank=True,null=True)
    class Meta:
        managed=False
        db_table='shop'
# Create your models here.
