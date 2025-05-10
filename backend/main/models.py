from django.contrib.auth.models import AbstractUser
from django.db import models


class EmailVerification(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    is_verified = models.BooleanField(default=False)
    verification_token = models.CharField(max_length=100, blank=True, null=True)
    token_created_at = models.DateTimeField(auto_now_add=True)


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Specification(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField()

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(null=True, blank=True, max_length=100)
    price = models.CharField(null=False, blank=False)
    image = models.ImageField(upload_to='product', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    specifications = models.ManyToManyField(Specification, blank=True)

    def __str__(self):
        return str(self.id) + ' - ' + str(self.name)
