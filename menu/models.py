from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Default Description")
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Snack(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Default Description")
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
