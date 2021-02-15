from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=105)
    product_price = models.CharField(max_length=67)
    product_dec = models.CharField(max_length=500)
    product_img = models.ImageField(upload_to="images")

    def __str__(self):
        return self.product_name

class cart(models.Model):
    product_cart = models.ForeignKey(product,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_cart.product_name



class profile(models.Model):
    user_detail = models.ForeignKey(User,on_delete=models.CASCADE)
    phon1 =  models.CharField(max_length=12,null=True)
    phon2 = models.CharField(max_length=12,null=True)
    address1 = models.CharField(max_length=70)
    address2 = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    state = models.CharField(max_length=70)
    zipcode = models.CharField(max_length=70)

    def __str__(self):
        return self.user_detail.username

