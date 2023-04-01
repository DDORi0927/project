from django.db import models
from django.utils import timezone

class Menu(models.Model):
    menu_type = models.ForeignKey("MenuType", on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/menu')
    status_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class MenuType(models.Model):
    menu_type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class OrderList(models.Model):
    menu_type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    number = models.IntegerField()
    payment = models.IntegerField()
    date_create = models.DateTimeField(default=timezone.now)
    status_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
# Create your models here.
