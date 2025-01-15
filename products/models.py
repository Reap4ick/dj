# from django.db import models


# # Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.EmailField()
#     birthdate = models.DateField()
#     username = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

from django.db import models


class Product(models.Model):
    CATEGORY_CHOICES = [
        (0, '1stCategory'),
        (1, '2stCategory'),
        (2, '3stCategory'),
    ]
        
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.IntegerField(choices=CATEGORY_CHOICES, default=0)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField( 
        max_length = 40, 
        choices = Product.CATEGORY_CHOICES, 
        default = 0) 

    def __str__(self):
        return self.name
