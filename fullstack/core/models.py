from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField()
    image_1 = models.ImageField(upload_to='images/', blank=True)
    image_2 = models.ImageField(upload_to='images/', blank=True)
    image_3 = models.ImageField(upload_to='images/', blank=True)

    def delete(self, *args, **kwargs):
        self.image_1.delete()
        self.image_2.delete()
        self.image_3.delete()
        super().delete(args, **kwargs)


class Contract(models.Model):
    # user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    # residence = models.ForeignKey(Residence, on_delete=models.DO_NOTHING)
    contract = models.FileField(upload_to='contracts/')
    residence_value = models.IntegerField()
    rented_at = models.DateField()
    closed_at = models.DateField(null=True)
    updated_at = models.DateField(null=True)

    def delete(self, *args, **kwargs):
        self.contract.delete()
        super().delete(args, **kwargs)