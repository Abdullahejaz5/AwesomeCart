from django.db import models

# Create your models here.
class Products (models.Model):
    #product_id=models.AutoField()

    product_name=models.CharField(max_length=50,default='')
    product_category=models.CharField(max_length=50,default='')
    product_price= models.IntegerField(default=0)
    product_desc=models.CharField(max_length=200,default='')
    product_pub_date=models.DateField()
    product_image=models.ImageField(upload_to='shop/images',default='')

    def __str__(self):
        return self.product_name
#django field reference

class Contact (models.Model):
    contact_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=50,default='')
    contact=models.CharField(max_length=50,default='')
    message=models.CharField(max_length=200,default='')

    def __str__(self):
        return self.name

class Order (models.Model):
    order_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50,default='')
    email=models.CharField(max_length=50,default='')
    contact=models.CharField(max_length=100,default='')
    address=models.CharField(max_length=500,default='')
    country=models.CharField(max_length=50,default='')
    state=models.CharField(max_length=50,default='')
    price=models.IntegerField(default=0)
    zip=models.CharField(max_length=200,default='')
    json_products=models.CharField(max_length=500,default='')

    def __str__(self):
        return self.name

class Update (models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.CharField(max_length=50,default='')
    order_status=models.CharField(max_length=50,default='')
    update_time=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.order_status[:7]+'.........'
