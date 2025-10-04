
from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # عکس‌ها داخل media/profile_pics/user_<id>/<filename>
    return f'profile_pics/user_{instance.user.id}/{filename}'

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # مهم: هر محصول به یک کاربر
    name = models.CharField(max_length=200,verbose_name="اسم :")
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name="قیمت :")
    quantity = models.IntegerField(verbose_name="تعداد :")
    image = models.ImageField(upload_to='product_images/', verbose_name="تصویر :")

    def __str__(self):
        return self.name
