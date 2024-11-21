from django.db import models
from purchase.models import Purchase
# Create your models here.
class Seller(models.Model):
    seller_id=models.CharField(max_length=1200)
    seller_name=models.CharField(max_length=120)
    seller_address=models.TextField()
    seller_contact=models.PositiveIntegerField()
    seller_email=models.EmailField()

    def __str__(self):
        return self.seller_id

class Category(models.Model):
    Type=models.CharField(max_length=256)

    def __str__(self):
        return self.Type

class Products(models.Model):
    product_id=models.CharField(max_length=1200,primary_key=True)
    product_name=models.CharField(max_length=500)
    product_type=models.ForeignKey(Category,on_delete=models.PROTECT)
    product_price=models.FloatField()
    product_image=models.ImageField(upload_to='product')
    product_seller=models.ForeignKey(Seller,on_delete=models.PROTECT)
    product_quantity=models.PositiveIntegerField(null=True)
    product_purchase_freq=models.PositiveIntegerField(null=True)

    def __str__(self):
        return self.product_id

