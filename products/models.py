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
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    category = models.CharField(max_length=255)
    photo = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name

