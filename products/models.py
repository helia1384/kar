from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="نام محصول :")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="قیمت :")
    quantity = models.IntegerField(verbose_name="تعداد :")
    image = models.ImageField(upload_to='product_images/', verbose_name="تصویر محصول :")


    def __str__(self):
        return self.name
